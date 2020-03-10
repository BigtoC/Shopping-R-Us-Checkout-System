# coding=utf-8

from modules import data

import sys


def calculate() -> float:
    """
    Get the counted SKUs and calculate the total price
    :return: The total price
    """
    price = 0.0

    for rule in data.specials:  # ToDo: Check match for each specials rule
        for k, v in data.sku_dict.items():
            if k in rule:
                price += analysis(k, v, rule)
            else:
                pass

    return price


def analysis(sku: str, num: int, rule: str) -> float:
    print(sku, num, rule)
    # Check the special rule case by case
    if "=" in rule:
        pass
    elif ">" in rule:
        pass
    else:
        sys.exit("Something wrong... Please check products_config.yaml and rerun the program")


if "__main__" == __name__:
    o = 0
    r = [
        '3 atv = 2 atv', '4 ipd = $499.99', '1 mbp > 1 vga', '5 vga = 4 vga'
    ]
    print([i for i, e in enumerate(r) if '499.99' in e])
