from math import sqrt

range1 = int(input("Enter the starting of range: "))
range2 = int(input("Enter the ending of range: "))
prime_list = []
count = 0


def check_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


for num in range(range1, range2):
    if check_prime(num):
        prime_list.append(num)

print(prime_list)

for j in range(0, len(prime_list)):
    for k in range(j + 1, len(prime_list)):
        if prime_list[k] - prime_list[j] == 6:
            # print(prime_list[j], prime_list[k])
            count += 1

print(count)
