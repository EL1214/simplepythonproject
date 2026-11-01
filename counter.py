#collections: counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
a = "aaaaabbbbccc"
counter = Counter(a)
print(counter)
print(counter.values())
print(counter.most_common(3)[1][0]) #print out one most common item

print(list(counter.elements()))