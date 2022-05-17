number = int(input())
count = 0
for num in range(1, 100):
    if number % num == 0:
        number += 1
        count += 1
    else:
        break
print(count)