# List Operations in Python
l = [10,20,30]
print(l)
# Output: [10, 20, 30]

l.append(40)
print(l)
# Output: [10, 20, 30, 40]

l.insert(2,25)
print(l)
# Output: [10, 20, 25, 30, 40]

l.pop()
# Output: 40

l.sort()
l.reverse()

print(l)
# Output: [30, 25, 20, 10]

l[0] = 35
print(l)
# Output: [35, 25, 20, 10]

l.remove(25)
print(l)
# Output: [35, 20, 10]