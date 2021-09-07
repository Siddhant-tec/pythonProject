numbers = list(map(int, input().rstrip().split()))
bits_count = list()


def check_bits():
    for number in numbers:
        bits_count.append(bin(number).count('1'))
    print(bits_count)
    print(sum(bits_count))

    bit_dict = dict((i, bits_count.count(i)) for i in bits_count)
    print(bit_dict)

    answer = 0
    for value in bit_dict.values():
        answer += value * (value - 1) // 2

    print(answer)


check_bits()
