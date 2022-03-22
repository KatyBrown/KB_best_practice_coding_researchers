a=list()
a.append(1)
a.extend([2, 3])

b = []
b = b + [1]
b += [2, 3]

def c():
    return [1, 2, 3]

print(a)
print (b)
print (c())