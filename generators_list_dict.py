names = [i for i in range(1, 10)]
print(names)
print(tuple(names))
names = {i: i**2 for i in range(1, 10)}
print(names)
names = {i for i in range(1, 10)}
print(names)
print(type(names))
names = (i for i in range(1, 10))
print(type(names))
