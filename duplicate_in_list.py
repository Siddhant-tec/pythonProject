nums = list(map(int, input().rstrip().split()))
dup = set(nums)
n = len(nums) - len(dup)

for element in dup:
    if element in nums:
        nums.remove(element)



print(nums)
print(n)
dict = {x: nums.count(x) + 1 for x in nums}
print(dict)