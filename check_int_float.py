items = ["a", 1, 2.5, "b"]
a = list()
for item in items:
    if isinstance(item, int):
        a.append(item)
    if isinstance(item, float):
        b.append(item)


print(a)

