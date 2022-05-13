n, min_candies = map(int, input().split())
candies = list(map(int, input().rstrip().split()))
#print(candies)
total = 0
for candy in candies:
    x = candy // min_candies
    total += x

print(total)
