from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(4)
d.append(4)
d.popleft()
d.extendleft([5,6,7])
print(d)
d.rotate(1) #to right
print(d)
d.rotate(-1) #to left
print(d)

#can append items from left or right