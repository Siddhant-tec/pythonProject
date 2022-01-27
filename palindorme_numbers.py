number = int(input())
sum = 0
for num in range(1, number+1):
    if str(num) != str(num)[::-1]:
        print(num)
        sum += num
print(sum)




