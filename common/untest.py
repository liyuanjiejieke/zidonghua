import unittest

from win32com.test.testall import verbosity


class TestUnit(unittest.TestCase):
    def test_case1(self):
        print("case1")
    def test_case2(self):
        print("case2")
class TestUnit2(unittest.TestCase):
    def test_case3(self):
        print("case3")
    def test_case4(self):
        print("case4")

def suite():
    # 创建一个集合
    suite=unittest.TestSuite()
    #该方法添加该类下的所有测试用例
    suite.addTest(TestUnit("test_case21"))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=1).run(suite())
    # unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(TestCase01('testThird_01'))
    # suite.addTest(TestCase01('testSecond_01'))
    # suite.addTest(TestCase01('testFirst_01'))
    # unittest.TextTestRunner().run(suite)  #根据case添加的顺序执行
