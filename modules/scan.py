# coding=utf-8

from collections import Counter


def scan(args: str) -> dict:
    """
    Accept a string as input and analysis the input SKUs
    :param args: Input of SKUs
    :return: A counted list
    """
    # Split the input by comma
    sku_list = args.split(", ")

    # Get element counts and convert to dict
    counted_dict = dict(Counter(sku_list))

    return counted_dict


if __name__ == "__main__":
    print(scan("atv, atv, atv, vga"))
