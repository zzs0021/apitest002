import requests, json,unittest


def readjson():
    datafile = "./data/data_json.json"

    with open(datafile, encoding="utf-8") as f:
        listdata = json.load(f)
        datalist = []
        for jsondata in listdata:
            case = jsondata.get("case")
            username = jsondata.get("username")
            password = jsondata.get("password")
            status = jsondata.get("status")
            result = jsondata.get("result")
            msg = jsondata.get("msg")

            datalist.append((case, username, password, status, result, msg))

    return datalist

def assertapi(self,status,result,msg,response):
    self.assertEqual(status,response.status_code)
    self.assertEqual(result,response.json().get("result"))
    self.assertIn(msg,response.json().get("msg"))
