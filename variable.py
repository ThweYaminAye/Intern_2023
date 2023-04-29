d_data = { "age": 23, "hobby": "coding"}
print(d_data["name"])
test = {"name":"Thwe","hobby":["coding","music","dance"],"grade":{
    "1st":"A",
    "2nd":"B",
    "3rd":"C"
}
}
print(test["name"])
print(test["hobby"][1])
print(test["grade"]["2nd"])
d_data.clear()
print(d_data)
x = test.copy()
print(x["name"])
A = {0,1,2}
x = 0
result = dict.fromkeys(A,x)
print(result)
re = result.get(0)
print(re)
mydata = d_data.items()
print(mydata)
print(d_data.keys())
print(d_data.values())
print(d_data.setdefault("name", "Yamin"))
print(d_data.items())
result = d_data.update({"name":"May Lamin"})
print(d_data)
result1 = d_data.update({"region":"shan"})
print(d_data)
x = d_data.copy()
print(x["region"])
y = x.get('region')
print(y)
print(d_data)
print(len(d_data))
# ncc = dict('name'="National Cyber City",'location'="pyin oo lwin")
# print(ncc)
# ncc["website"]="ncc.com"
# print(ncc)
