x = ['x', 0, 2, 3, 4, 6]
print(x.__len__())

enumerate(x)
for index, value in enumerate(x, start=1):
    print(f"{index:3d}: {value}")

print(all(x))
print(any(x))
print(hasattr(x, 'x'))
