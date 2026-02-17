import json

# with open("data.json", "r") as fff:
#     data = json.load(fff)
#     print(type(data))
#     print(data)
#     print(data["users"])

#     for i in data["users"]:
#         print(i["name"])
#load, loads, dump, dumps

# with open("data.json", "r+") as fff:
#     data = json.load(fff)
#     data["users"].append({"id": 4, "name": "Amelia", "age": 19})
#     print(data)
#     fff.seek(0)
#     json.dump(data, fff, indent = 2)


# with open("data.json", "r+") as fff:
#     data = json.load(fff)
#     for i in data["users"]:
#         if i["name"] == "John":
#             i["age"] = 30
#     fff.seek(0)
#     json.dump(data, fff, indent = 2)


# data = '{"owners" : [{"id":1, "name":"Ynker Hovsepyan"}, {"id":2, "name":"Epstein"}]}'
# print(json.loads(data))

# with open("data.json", "r+") as f:
#     s = f.read()
#     print(s)
    # print(json.loads(f.read()))

#loads(string) տողի մեջ գրված json  օբյեկտը դարձնում է dictionary
#load(file pointer) ֆայլի մեջ գրված json  օբյեկտը դարձնում է dictionary\
b = "b"
d = {"a": 1, b : 2}
s = json.dumps(d)
print(s)
print(type(s))