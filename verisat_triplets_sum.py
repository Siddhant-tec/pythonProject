numbers = list(map(int, input().rstrip().split()))
value = int(input())
sum = 0
answer = list()
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] < value:
                sum += 1

print(sum)