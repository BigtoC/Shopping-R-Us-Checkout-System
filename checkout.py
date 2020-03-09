# coding=utf-8

from modules import scan
from modules import specials

import sys


def print_help():
    """
    Print the hints for this program
    :return: None
    """
    print("Run this program: python checkout.py --run")
    print("Exist this program: python checkout.py --end")
    print("Change specials rules: Read the README document")


def main():
    """
    Perform the main function of this program
    :return: None
    """
    args: str = input("SKUs Scanned: ")
    sku_dict: dict = scan.scan(args)
    price: float = specials.calculate(sku_dict)

    print(f"Total expected: ${price}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1].strip().lower() == "--help":
        print_help()
    if len(sys.argv) < 2 or sys.argv[1].strip().lower() == "--end":
        sys.exit("The checkout program has been ended")
    if len(sys.argv) < 2 or sys.argv[1].strip().lower() == "--run":
        main()
