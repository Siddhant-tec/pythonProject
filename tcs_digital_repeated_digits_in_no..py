start = int(input())
end = int(input())
nums = list(map(str, range(start, end+1)))


def has_doubles(nums):
    count = 0
    for number in nums:
        if len(number) == 2:
            if number[0] == number[1]:
                print(number)
                count += 1
            else:
                continue
        if len(number) == 3:
            if number[0] == number[1] == number[2]:
                print(number)
                count += 1
            elif number[0] == number[1] or number[1] == number[2] or number[2] == number[0]:
                print(number)
                count += 1
            else:
                continue
    print("No of repeated digits is: ", count)
    print("No of non-repeated digits is: ", len(nums) - count)


has_doubles(nums)
