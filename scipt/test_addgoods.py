import requests,unittest,logging
from parameterized import parameterized
from read_json.read_addgood import addgoods
from api.addgoods import addgoods_api
from assert01 import assertapi

class AddGoods(unittest.TestCase):
    @parameterized.expand(addgoods)
    def test_addgood(self,case,goods_name,category_id,status,result,msg):
           response = addgoods_api(goods_name,category_id)
           assertapi(self, status, result, msg, response)
           logging.info("{0}:{1}".format(case, response.json()))