import  requests


session =requests.session()
def loginapi():
  url="http://192.168.1.160:5000/login"
  data = {"username":"lucy","password":"123456"}
  header = {"Content-Type":"application/json"}

  response = session.post(url,headers=header,json=data)

  #return response

b=loginapi()
print(b)



