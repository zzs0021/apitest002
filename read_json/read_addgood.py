import  requests,json

def addgoods():
    addgood = "./data/data_addgoods.json"
    with open(addgood,encoding="utf-8")  as   f:
        addgoodlist = json.load(f)
        addgoods_list=[]
        for json_data  in addgoodlist:
            case = json_data.get("case")
            goods_name = json_data.get("goods_name")
            category_id = json_data.get("category_id")
            status = json_data.get("status")
            result = json_data.get("result")
            msg = json_data.get("msg")

            addgoods_list.append((case,goods_name,category_id,status,result,msg))

    return addgoods_list