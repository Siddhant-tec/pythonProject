numbers = list(map(int, input().rstrip().split()))
answer = list()
n = len(numbers)
for i in range(n):
    for j in range(i+1, n):
        if numbers[i] < numbers[j]:
            answer.append(numbers[j])

print(answer)



