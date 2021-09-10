numbers = list(map(int, input().rstrip().split()))
count = 0
answer = []
d = dict()
for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        sum = numbers[i] + numbers[j]
        x = (numbers[i], numbers[j])
        if sum in numbers:
            if numbers[i] != numbers[j]:
                d[x] = 1
                print(numbers[i], numbers[j])
                count += 1
        else:
            continue
if len(d.keys()) == 0:
    print(1)
else:
    print(len(d.keys()))

