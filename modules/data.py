# coding=utf-8

import yaml
import os

args: str = ""  # The input SKUs
sku_dict: dict = {}  # Counted SKUs
product_data: dict = {}
products = {}
specials = {}


def read_file():
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
    :return: None
    """
    # Get the absolute path of the file
    json_path = os.path.dirname(__file__)
    rel_path = "../products_config.yaml"
    abs_json_path = os.path.join(json_path, rel_path)

    global product_data, products, specials

    # Read the file
    with open(abs_json_path, "r") as file:
        product_data = yaml.safe_load(file)

        products = product_data["Products"]
        specials = product_data["Specials"]
