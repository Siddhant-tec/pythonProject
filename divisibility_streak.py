def streak(number):
    count = 0
    for num in range(1, 100):
        if number % num == 0:
            number += 1
            count += 1
        else:
            break
    return count


s = int(input())
number = int(input())
count = 0
while(number > 0):
    if streak(number) == s:
        count += 1
    number -= 1

print(count)