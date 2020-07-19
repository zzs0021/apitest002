from api.login import session
import requests

def addgoods_api():
    url= "http://192.168.1.160:5000/addgoods"
    data ={
            "goods_name":"huawei mate10",
             "category_id": 1,
             "main_image":"dfsfsfsafs",
             "price":"1680",
             "quantity":999,
              "detail":"dffdsfsfsf",
               "status":1,}
    header= {"Content-Type":"application/json"}


    response =session.post(url,json=data,headers=header)

    return response
a=addgoods_api()
print(a)


a=addgoods_api()
print(a)
