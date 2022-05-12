inp = int(input())
while inp > 0:
    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    lst = [i ** 2 for i in numbers]
    lst.sort()
    ans = 0

    for x in lst:
        for y in lst:
            if (x + y) in lst:
                ans += 1

    if ans > 0:
        print(True)
    else:
        print(False)

    inp -= 1
