halts = list(map(int, input().rstrip().split()))
y = int(input())


def skip():
    max_time = max(halts)
    for num in range(len(halts)):
        if halts[num] == max_time:
            if halts[num + 1] > halts[num - 1]:
                return halts[num + 1]
            else:
                return halts[num - 1]



def min_time():
    halts2 = halts.copy()
    halts2.remove(max(halts))
    halts2.remove(skip())
    answer1 = sum(halts2)
    result = answer1 + min(max(halts), y) + min(skip(), y)
    print(result)

min_time()