


#  1.放在当前的项目下，为了导包


#2.导入 HTMLTestRunner 类
"""
就是把unittest.TxtTestRunner  做一个加强，
主要是把测试结果写到了一个HTML文件中，但是保留了TxtTestRunner
"""

import unittest
from HTMLTestRunner import HTMLTestRunner  #导入包



suite = unittest.TestLoader().discover('.', pattern='test*.py')   #生成测试套件

report_path = "./test_report.html"  #设置报告生成路径和文件名

with open(report_path,'wb') as f:  #打开报告
    runner = HTMLTestRunner(f,title='测试报告',description="v1.0")  #实例化HTMLTestRunner对象
    runner.run(suite)