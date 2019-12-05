#这是一种简单的线性测试，非模块化测试，从main开始依次运行

import unittest
from function import *

class TestFunc(unittest.TestCase):
    # 继承自unittest.TestCase
    # 重写TestCase的setUp()、tearDown()方法：在每个测试方法执行前以及执行后各执行一次
    def setUp(self):
        print("do something before test : prepare environment")

    def tearDown(self):
        print("do something after test : clean up ")

    # 测试方法均已test开头，否则是不被unittest识别的
    @unittest.skip("This  is just a try because I don't want to test it")
    def test_add(self):
        print("add test:")
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        print("minus test")
        self.assertEqual(3, minus(5, 2))

    def test_multi(self):
        print("multi test")
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        print("divide test")
        self.assertEqual(2, divide(4, 2))


if __name__ == "__main__":
    # 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)