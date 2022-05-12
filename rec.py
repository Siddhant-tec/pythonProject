l = [1, 2, 3, 4, 5]


def reverse(l):
    if len(l) == 1:
        return l
    return [l.pop()] + reverse(l)

print(reverse(l))