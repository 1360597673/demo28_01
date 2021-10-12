


import unittest
from controler import  login


class Testlogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:  #初始化，整个类开始前才会运行一次
    #     print('开始执行测试用例')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:  #清空， 整个类结束才会运行一次
    #     print("测试用例执行完毕")


    # def setUp(self) -> None:    #初始化 ，每个方法运行前都会运行一次
    #     print('初始化用例')
    # def tearDown(self) -> None:  #清空，每个方法运行前都会清空一次
    #     print('清空')

    def test_login1(self):

        self.assertEqual('登录成功',login('admin','123456'))

    def test_login2(self):

        self.assertEqual('用户名不能为空', login(' ','123456'))

    def test_login3(self):

        self.assertEqual('密码为空', login('admin', ' '))


suite = unittest.TestSuite()
# suite.addTest(Testlogin('test_login2'))
# suite.addTest(Testlogin('test_login3'))   #一次添加一个用例


case_list = [Testlogin('test_login2'),Testlogin('test_login3')]

suite.addTests(case_list)   # 一次添加多个用例

runner = unittest.TextTestRunner(verbosity = 2)

#verbosity参数可以控制输出的错误报告的详细程度，只有 3 个取值：
#0 (quiet): 只显示执行的用例的总数和全局的执行结果。
#1 (default): 默认值，显示执行的用例的总数和全局的执行结果，并对每个用例的执行结果（成功 T 或失败 F）有个标注。
#2 (verbose): 显示执行的用例的总数和全局的执行结果，并输出每个用例的详细的执行结果。


runner.run(suite)

# suite_smoke = unittest.TestSuite()
# suite_smoke.addTest(Testlogin('test_login1'))


