nums = list(input().rstrip().split())


def has_doubles(nums):
    for number in nums:
        if number[0] == number[1]:
            print(number)
        else:
            continue


has_doubles(nums)