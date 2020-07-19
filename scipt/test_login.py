from assert01 import readjson,assertapi
from api.login import loginapi
from parameterized import parameterized
import unittest,requests,logging
from config import Initlog


class LoginApi(unittest.TestCase):
    @parameterized.expand(readjson)
    def test_login(self,case,username,password,status,result,msg):
        response =loginapi(username,password)
        assertapi(self,status,result,msg,response)
        logging.info("{0}:{1}".format(case,response.json()))
