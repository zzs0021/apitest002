import requests


url = "http://192.168.1.160:5000/login"
data = {"username":"lucy","password":"123456"}
headers = {"Content-Type":"application/json"}
session =requests.session()

r=session.post(url,json=data,headers=headers)

print(r.json())

data ={
"goods_name":"xiaominote4",
"main_image":"dfsfsfsafs",
"price":"1680",
"quantity":999,
"detail":"dffdsfsfsf",
"status":1,
"category_id":1
}
url="http://192.168.1.160:5000/addgoods"
r=session.post(url,json=data,headers=headers)
print(r.json())
