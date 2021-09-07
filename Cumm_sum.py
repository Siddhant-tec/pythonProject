x = int(input())
numbers = list()
for i in range(x):
    inp = int(input())
    numbers.append(inp)
#numbers = list(map(int, input().rstrip().split()))
answer = []
sum = 0
for i in range(0, len(numbers)):
    sum += numbers[i]
    answer.append(sum)

print(answer)
