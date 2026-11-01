dict = {"name":"Max","age":20,"city":"Ingolstadt"}

dict["name"] = "S"
dict["email"] = "max9@gmail.com"
dict.popitem()
print(dict)

if "age" in dict:
    print(dict["age"])

try:
    print(dict["country"])
except:
    print(False)

for key,value in dict.items():
    print(key,value)
