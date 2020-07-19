import unittest,time
from scipt.test_login import LoginApi
from scipt.test_addgoods import AddGoods
from tools.HTMLTestRunner import HTMLTestRunner


suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginApi))
suite.addTest(unittest.makeSuite(AddGoods))

filename = "./report/yuze{}.html".format(time.strftime("%Y%m%d  %H%M%S"))

with open( filename,"wb") as f :
    runner = HTMLTestRunner(f,title="接口自动化测试报告",description="宇泽登录接口")
    runner.run(suite)