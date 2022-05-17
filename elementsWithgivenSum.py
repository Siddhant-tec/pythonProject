numbers = list(map(int, input().rstrip().split()))
sum1 = int(input())
ans = []
for i in range(1, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == sum1:
            ans.append([i, j])
print(ans)