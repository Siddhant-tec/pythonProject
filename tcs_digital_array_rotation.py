numbers = list(map(int, input().rstrip().split()))
r = int(input())


def left_array_rotate():
    old = numbers[:r].copy()
    new = numbers[r:].copy()
    print(new + old)


def right_array_rotate():
    r2 = len(numbers) - r
    old = numbers[:r2].copy()
    new = numbers[r2:].copy()
    print(new + old)


print(numbers)
right_array_rotate()
left_array_rotate()
