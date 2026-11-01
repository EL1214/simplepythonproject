add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x * y
print(mult(10,5)) #for function used only once in the code

list2 = [(1,10),(15,1),(5,-1),(10,4)]
print(sorted(list2)) #sorted default by x index
print(sorted(list2, key = lambda x: x[1])) #sorted by y index
print(sorted(list2, key = lambda x: x[0] + x[1])) #sorted by the sum of indexes


#map
a = [1, 2, 3, 4, 5]
b1 = map (lambda x: x*2, a) #using map
print(list(b1))

c1 = [x * 2 for x in a] #using list
print(c1)

b2 = filter(lambda x: x%2 == 0, a)
print(list(b2))

c2 = [x for x in a if x % 2 == 0]
print(c2)


