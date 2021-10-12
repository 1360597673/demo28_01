

import unittest
from controler import  login
from  parameterized import parameterized


class Testlogin(unittest.TestCase):


    @parameterized.expand([("登录成功",'admin','123456'),('用户名不能为空', ' ','123456'),('密码不能为空', 'admin', ' ')])
    def test_loing(self,expect,username,password):
        self.assertEqual(expect,login(username,password))







