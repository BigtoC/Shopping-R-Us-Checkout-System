# coding=utf-8

import unittest

from modules import specials
from modules import data
from modules import scan


class TestPrice(unittest.TestCase):

    def test_3atv_1vga(self):
        data.args = "atv, atv, atv, vga"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 249.00

        self.assertEqual(expected_result, actual_result)

    def test_2atv_5ipd(self):
        data.args = "atv, ipd, ipd, atv, ipd, ipd, ipd"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 2718.95

        self.assertEqual(expected_result, actual_result)

    def test_1mbp_1vga_1ipd(self):
        data.args = "mbp, vga, ipd"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 1949.98

        self.assertEqual(expected_result, actual_result)

    def test_2mbp_2vga_1ipd(self):
        data.args = "mbp, vga, mbp, vga, ipd"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 3349.97

        self.assertEqual(expected_result, actual_result)

    def test_6vga_1ipd(self):
        data.args = "vga, vga, vga, vga, vga, vga, ipd"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 699.99

        self.assertEqual(expected_result, actual_result)

    def test_1vga_3atv(self):
        data.args = "atv, atv, atv, vga"
        data.read_file()
        scan.scan()
        actual_result = specials.calculate()
        expected_result = 249

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
