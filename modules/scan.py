# coding=utf-8

from modules import data

from collections import Counter


def scan() -> dict:
    """
    Accept a string as input and analysis the input SKUs
    :return: A counted list
    """
    # Split the input by comma
    sku_list = data.args.split(", ")

    # Get element counts and convert to dict
    data.sku_dict = dict(Counter(sku_list))

    return data.sku_dict


if __name__ == "__main__":
    data.args = "atv, atv, atv, vga"
    print(scan())
