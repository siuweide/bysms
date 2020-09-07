import json
a = {"ret": 1, "msg": "action\u53c2\u6570\u9519\u8bef"}
str_a = json.dumps(a)
print(json.loads(str_a))