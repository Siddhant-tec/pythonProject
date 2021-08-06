nk = input().split()
n = int(nk[0])
k = int(nk[1])
list = list(map(int, input().rstrip().rsplit()))


def check_pairs():
    count = 0
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if abs(list[j] - list[i]) == k:
                count += 1
    print(count)


check_pairs()
