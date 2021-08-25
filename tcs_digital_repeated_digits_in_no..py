nums = list(input().rstrip().split())


def has_doubles(nums):
    for number in nums:
        y = ''.join(number)
        if y[0] == y[1]:
            print(number)
        else:
            continue


has_doubles(nums)
