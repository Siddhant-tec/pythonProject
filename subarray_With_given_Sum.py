numbers = list(map(int, input().rstrip().split()))
target = int(input())

sum_now = list()
answer = list()
count = 0

for i in range(len(numbers)):
    sum_now.append(numbers[i])
    if sum(sum_now) == target:
        count += 1
        sum_now.clear()



print(count)
