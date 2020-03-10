# coding=utf-8

from modules import scan
from modules import specials
from modules import data

import sys


def print_help():
    """
    Print the hints for this program
    :return: None
    """
    print("Change specials rules: Read the README document")
    print("Also available online : https://github.com/BigtoC/Shopping-R-Us-Checkout-System/blob/master/README.md")


def main():
    """
    Perform the main function of this program
    :return: None
    """
    data.read_file()  # Init the specials data in the YAML file
    data.args = input("SKUs Scanned: ")
    scan.scan()
    price: float = specials.calculate()

    print(f"Total expected: ${price}")


if __name__ == "__main__":

    cmd = input(
        "Input 'help' to read the instruction. \n"
        "Input 'run' to execute the main function. \n"
        "Input 'end' to exist this program. \n\n"
        "PLease input your command: "
    )

    if cmd == "help":
        print_help()
    elif cmd == "run":
        main()
    elif cmd == "end":
        sys.exit("The checkout program has been ended.")
    else:
        sys.exit("Wrong command! Please rerun this program with the correct command.")

