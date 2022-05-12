numbers = [1, 2, 3, 4, 5]
i = len(numbers)


def minimum(numbers, n):
    if n == 1:
        return numbers[0]
    return max(numbers[n - 1], minimum(numbers, n - 1))


print(minimum(numbers, i))