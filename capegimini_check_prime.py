import math

number = int(input())


def is_prime(number):
    x = int(math.sqrt(number))
    for i in range(2, number):
        if number % i == 0:
            print("Prime")
            break
        else:
            print("Not Prime")
            break


is_prime(number)
