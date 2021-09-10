numbers = list(map(int, input().rstrip().split()))
sum = 0
target = int(input())
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        sum = numbers[i] + numbers[j]
        diff = sum - target
