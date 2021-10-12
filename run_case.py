
import unittest

# 组装套件的入口


#1，创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')

# 2. 创建运行器
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
