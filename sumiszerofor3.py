#-10 6 7 -13 8 2
numbers = list(map(int, input().rstrip().split()))
print(numbers)
answer = list()
ans = 0
for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == 0:
                answer.append([a, b, c])
                ans += 1
if ans > 1:
    res = list(set(tuple(sorted(sub)) for sub in answer))
    x = [list(i) for i in res]
    print(x)