# coding=utf-8

from modules import data

import sys


def calculate() -> float:
    """
    Get the counted SKUs and calculate the total price
    :return: The total price
    """
    price = 0.0
    rule_num = len(data.specials)
    checked_list = []

    for sku, num in data.sku_dict.items():
        for i in range(rule_num):
            matched = 0
            rule = data.specials[i]
            last_price = price
            # print(f"sku: {sku}, rule: {rule}, price: {price}")
            if sku == rule.split(" ")[1]:  # 'atv' in '3 atv = 2 atv'[1]
                price += analysis(sku, num, rule)
                if price > last_price:  # If true, means the price has been updated
                    matched += 1  # Update the status of rule matched
                    checked_list.append(sku)  # append the checked sku

            elif i == rule_num - 1 and matched == 0 and sku not in checked_list:  # Calculate those not match rules
                price += data.products[sku]["price"] * num

    return round(price, 2)


def analysis(sku: str, num: int, rule_str: str) -> float:
    """
    Analysis sku with specials rule in different scenarios, and calculate the price
    :param sku: The current sku
    :param num: Quantity of this sku
    :param rule_str: Current rule for analysis
    :return: The price of current sku
    """
    price = 0.0
    rule_list = rule_str.split(" ")  # Convert str to list
    current_sku_price = data.products[sku]["price"]

    # Check the special rule case by case
    if "=" in rule_str:
        if sku == rule_list[1]:  # 'atv' in '3 atv = 2 atv'
            require_num = int(rule_list[0])
            if num >= require_num:  # no. of 'atv' = 4, >= 3
                remain_num = num % require_num  # 4 % 3 = 1
                remain_price = remain_num * current_sku_price  # 1 * 109.5

                if "$" in rule_str:  # '4 ipd = $499.99'
                    # Suppose 5 ipd scanned: remain_num = 5 % 4 = 1, remain_price = 549.99 * 1
                    price = float(rule_list[-1].replace("$", "")) * num  # 499.99 * 5
                else:
                    special_product = rule_list[-1]  # special_product = 'atv'
                    this_special_price = data.products[special_product]["price"]  # atv price = 109.5
                    special_num = int(rule_list[-2])  # special_num = 2
                    price = this_special_price * special_num + remain_price  # 109.5 * 2 + 109.5
            else:  # If not match the rule, return the original price
                price = current_sku_price * num

    elif ">" in rule_str:
        if sku == rule_list[1]:  # 'mbp' in '1 mbp > 1 vga'
            if num >= int(rule_list[0]):  # no. of mbp = 2, >= 2
                special_product = rule_list[-1]  # special_product = vga
                if special_product in data.args:  # 'vga' in 'mbp, vga, ipd'
                    special_num = int(num / int(rule_list[0]))
                    tmp_price = data.products[sku]["price"] * num  # tmp_price = mbp * 1

                    # Subtract the price of vga from the total price of mbp
                    special_price = data.products[special_product]["price"] * special_num
                    price = tmp_price - special_price
            else:  # If not match the rule, return the original price
                price = current_sku_price * num

    else:
        sys.exit("Something wrong... Please check products_config.yaml and rerun the program")
    return price


if "__main__" == __name__:
    o = 0
    r = [
        '3 atv = 2 atv', '4 ipd = $499.99', '1 mbp > 1 vga', '5 vga = 4 vga'
    ]
    sp = r[0].split(" ")
