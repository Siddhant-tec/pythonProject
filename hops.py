n = int(input())
path = list(map(int, input().rstrip().split(', ')))


def single_jump(i):
    for i in range(0, len(path)-1):
        if n >= 2:
            i += 1
    return 2 * (path[i])


def double_jump(i):
    for i in range(0, len(path)-1):
        if n >= 3:
            i += 2
    return 3 * (path[i])


def score():
    points = []
    max_no = max(path)
    for i in range(0, len(path)-1):
        if n >= 3:
            x = max(max_no, double_jump(i), single_jump(i))
            points.append(x)
            i += 1
        else:
            return sum(path)
    return sum(points)


print(score())





#score()
print(score())
