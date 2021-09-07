numbers = list(map(int, input().rstrip().split()))


def bitscount():
    max_no = max(numbers)
    i = 0
    k = 0

    bits = [0 for i in range(max_no + 1)]
    i = 1

    while i <= max_no:
        bits[i] = 1
        i *= 2

    print(bits)

    for i in range(1, max_no + 1):
        if bits[i] == 1:
            k = 1
        if bits[i] == 0:
            bits[i] = bits[k] + bits[i - k]
    print(bits)

    bits_dict = dict()

    for number in range(len(numbers)):
        x = bits[numbers[number]]
        if x in bits_dict:
            bits_dict[x] += 1
        else:
            bits_dict[x] = 1

    result = 0
    for n in bits_dict.values():
        result += n * (n - 1) // 2

    print(result)


bitscount()
