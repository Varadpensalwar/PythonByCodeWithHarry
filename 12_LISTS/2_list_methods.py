a = [4,65,7,"vars"]
a[1]=34
a.pop()
a.append("varad")
a.insert(1,56)
# print(a)

b = [4,5,7,89,8,8]
a.extend(b)
# print(a)

# print(b.count(8))
b.sort()
# print(b)
print(b.index(4))

c=b.copy()
b.clear()
print(b)
print(c)