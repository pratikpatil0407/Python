l = [1,2,3,4]

print(l[0:2])

l.append(5)
print(l)

l.insert(1,77)
print(l)

l.remove(77)
print(l)

l.pop()
print(l)

l = [1,2,3,2]
count = l.count(2)
print(count)

l.sort()
print(l)

print(len(l))

l2 = l.copy()
print(l2)

l.clear()
print(l)