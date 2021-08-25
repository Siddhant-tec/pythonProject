start = int(input())
end = int(input())
nums = list(map(str, range(start, end+1)))


def has_doubles(nums):
    for number in nums:
        if len(number) == 2:
            if number[0] == number[1]:
                print(number)
            else:
                continue
        if len(number) == 3:
            if number[0] == number[1] == number[2]:
                print(number)
            else:
                continue


has_doubles(nums)
