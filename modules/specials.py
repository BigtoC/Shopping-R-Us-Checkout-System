# coding=utf-8

import yaml
import os
import sys


def calculate(sku_list: dict) -> float:
    """
    Get the counted SKUs and calculate the total price
    :param sku_list: The counted SKUs
    :return: The total price
    """
    price = 0.0
    product_data = read_file()

    products = product_data["Products"]
    specials = product_data["Specials"]

    for rule in specials:  # ToDo: Check match for each specials rule
        for k, v in sku_list.items():
            if k in rule:
                analysis(k, v, rule)
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


def read_file() -> dict:
    """
    Read the YAML file, the structure is shown below
    {'Products: {
        'ipd': {'name': 'Super iPad', 'price': 549.99},
        'mbp': {'name': 'MacBook Pro', 'price': 1399.99},
        'atv': {'name': 'Apple TV', 'price': 109.5},
        'vga': {'name': 'VGA adapter', 'price': 30.0}
    }
    'Specials': [
        '3 atv = 2 atv', '4 ipd = $499.99', '1 mbp > 1 vga', '5 vga = 4 vga'
    ]}
    :return: Data in the YAML file as a dict
    """
    # Get the absolute path of the file
    json_path = os.path.dirname(__file__)
    rel_path = "../products_config.yaml"
    abs_json_path = os.path.join(json_path, rel_path)

    # Read the file
    with open(abs_json_path, "r") as file:
        product_data = yaml.safe_load(file)

    return product_data


if "__main__" == __name__:
    o = 0
    l = [
        '3 atv = 2 atv', '4 ipd = $499.99', '1 mbp > 1 vga', '5 vga = 4 vga'
    ]
    print([i for i, e in enumerate(l) if '499.99' in e])
