nums = list(map(int, input().rstrip().split()))
print(nums)
sums = list()
sum = 0
count = 0
for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += nums[j]
        #sums.append(sum)
        if sum == 0:
            count += 1

#print(sum)
print(sums)
print(count)
