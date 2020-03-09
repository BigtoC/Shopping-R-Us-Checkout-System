# coding=utf-8

import yaml
import os


def calculate(sku_list: dict) -> float:
    """
    Get the counted SKUs and calculate the total price
    :param sku_list: The counted SKUs
    :return: The total price
    """
    json_path = os.path.dirname(__file__)
    rel_path = "../products_data.yaml"
    abs_json_path = os.path.join(json_path, rel_path)

    price = 0.0

    with open(abs_json_path, "r") as file:
        product_data = yaml.safe_load(file)

    products = product_data["Products"]
    specials = product_data["Specials"]

    for k, v in sku_list.items():
        price += products[k]["price"] * v

    # ToDo: Specials analysis
    return price


"""
{
    'ipd': {'name': 'Super iPad', 'price': 549.99}, 
    'mbp': {'name': 'MacBook Pro', 'price': 1399.99}, 
    'atv': {'name': 'Apple TV', 'price': 109.5}, 
    'vga': {'name': 'VGA adapter', 'price': 30.0}
}
['3 atv = 2 atv', '4 ipd = $499.99', '1 mbp > 1 vga', '5 vga = 4 vga']
"""

