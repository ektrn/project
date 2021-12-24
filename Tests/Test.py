import unittest
import sys
from random import randint
from time import time
from FileHandler import *


def fill_file_by_random(path, numbers_count):
    f = open(path, "w")
    for i in range(0, numbers_count):
        f.write(str(randint(-1000000000, 1000000000)))
        if i != numbers_count - 1:
            f.write(" ")
    f.close()

class SumTest(unittest.TestCase):

    def test_sum1(self):
        file_handler = FileHandler("test1.txt")
        self.assertEqual(file_handler.get_sum(), 10)

    def test_sum2(self):
        file_handler = FileHandler("test2.txt")
        self.assertEqual(file_handler.get_sum(), -10)

    def test_sum3(self):
        file_handler = FileHandler("empty.txt")
        self.assertEqual(file_handler.get_sum(), 0)

    def test_sum4(self):
        file_handler = FileHandler("test3.txt")
        self.assertEqual(file_handler.get_sum(), 0)


class ProdTest(unittest.TestCase):

    def test_prod1(self):
        file_handler = FileHandler("test1.txt")
        self.assertEqual(file_handler.get_product(), 25)

    def test_prod2(self):
        file_handler = FileHandler("test2.txt")
        self.assertEqual(file_handler.get_product(), 1800)

    def test_prod3(self):
        file_handler = FileHandler("empty.txt")
        self.assertEqual(file_handler.get_product(), "no numbers")

    def test_prod4(self):
        file_handler = FileHandler("test3.txt")
        self.assertEqual(file_handler.get_product(), 0)


class MinTest(unittest.TestCase):

    def test_min1(self):
        file_handler = FileHandler("test1.txt")
        self.assertEqual(file_handler.get_min(), 5)

    def test_min2(self):
        file_handler = FileHandler("test2.txt")
        self.assertEqual(file_handler.get_min(), -10)

    def test_min3(self):
        file_handler = FileHandler("empty.txt")
        self.assertEqual(file_handler.get_min(), "no minimum")

    def test_min4(self):
        file_handler = FileHandler("test3.txt")
        self.assertEqual(file_handler.get_min(), 0)


class MaxTest(unittest.TestCase):

    def test_max1(self):
        file_handler = FileHandler("test1.txt")
        self.assertEqual(file_handler.get_max(), 5)

    def test_max2(self):
        file_handler = FileHandler("test2.txt")
        self.assertEqual(file_handler.get_max(), 10)

    def test_max3(self):
        file_handler = FileHandler("empty.txt")
        self.assertEqual(file_handler.get_max(), "no maximum")

    def test_max4(self):
        file_handler = FileHandler("test3.txt")
        self.assertEqual(file_handler.get_max(), 0)


class SpeedTest(unittest.TestCase):
    @staticmethod
    def runCommands(path):
        file_handler = FileHandler(path)
        file_handler.get_numbers_as_string()
        file_handler.get_min()
        file_handler.get_max()
        file_handler.get_sum()
        file_handler.get_product()

    def test_speed1(self):
        path = "big_file.txt"
        fill_file_by_random(path, 20000)
        start_time = time()
        SpeedTest.runCommands(path)
        sys.stdout.write(f'20000 numbers took {time()-start_time} seconds \n')

    def test_speed2(self):
        path = "big_file.txt"
        fill_file_by_random(path, 10000)
        start_time = time()
        SpeedTest.runCommands(path)
        sys.stdout.write(f'10000 numbers took {time()-start_time} seconds \n')

    def test_speed3(self):
        path = "big_file.txt"
        fill_file_by_random(path, 5000)
        start_time = time()
        SpeedTest.runCommands(path)
        sys.stdout.write(f'5000 numbers took {time()-start_time} seconds \n')


class FileNameTest(unittest.TestCase):
    def test_filename1(self):
        file_handler = FileHandler("fefdhehehe")
        self.assertEqual(file_handler.fileExist, False)

    def test_filename2(self):
        file_handler = FileHandler("fefdhehehe.txt")
        self.assertEqual(file_handler.fileExist, False)

    def test_filename3(self):
        file_handler = FileHandler("empty.txt")
        self.assertEqual(file_handler.fileExist, True)


if __name__ == '__main__':
    unittest.main()
