list1 = [2,6,7,4,3,-1]
print(list1)
print(list1[-1])

#appending at last
list1.append("d")
print(list1)

#insert in specific positions
list1.insert(2, 3)
print(list1)

#remove items at last
list1.pop()
print(list1)

#remove a specific items
item = list1.remove(3)
print(list1)

new = sorted(list1)
print(new)

zero = [0] * 5
print(zero)

print(zero + new)

print(list1[1:5])
print(list1[1::2])

#duplicate list
org = ["a","b","c"]
copy = org.copy() #list(org)
copy.append("d")
print(org)
print(copy)

#list comprehension
a = [1,2,3,4]
b = [i * i for i in a]
print(b)