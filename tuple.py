t = (1,1,1,1,1,2,2,2,"g",3,3,4)
print(t)

t1 = ("a",)
print(type(t1))

print(t[3])

if "h" in t:
    print(True)
else:
    print(False)

print(t.count(1))
print(t.index("g"))

print(list(t))

t1 = ("Max", 28, "Ingolstadt","85051")
name, *data, postcode = t1
print(data)

#tuple are move efficient than list when doing large data