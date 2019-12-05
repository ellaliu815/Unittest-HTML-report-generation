#使用test suite来进行封装测试

import unittest
from testsample import *
import HtmlTestRunner

if __name__ == "__main__":
    filepath = '../report'    #This is the folder of HTML test report
    suite = unittest.TestSuite()  #例化test suite

#creat the test list,按照这个顺序来执行测试用例
tests = [TestFunc("test_add"),TestFunc("test_minus"), TestFunc("test_multi"), TestFunc("test_divide")]

suite.addTests(tests) #将测试用例封装成一个suite

#这是一种输出结果的方法
#runner = unittest.TextTestRunner(verbosity=2) #加载runner,verbosity = 0 :no test result report
                                              #                     = 1 :have test result report, but not detail
                                              #                     = 2: have detail result report

#这是采用HTML输出测试结果的方法
runner = HtmlTestRunner.HTMLTestRunner(output=filepath,verbosity=2)
runner.run(suite)







