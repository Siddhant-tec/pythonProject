n = int(input())


def arrangements(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return (n - 1) * (arrangements(n - 1) + arrangements(n - 2))


print(arrangements(n))
