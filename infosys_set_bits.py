numbers = list(map(int, input().rstrip().split()))
n = len(numbers)
sorted_list = list()
for i in range(n):
    for j in range(i+1, n):
        if bin(numbers[i]).count("1") == bin(numbers[j]).count("1"):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print(numbers[i], numbers[j])

print(numbers)
