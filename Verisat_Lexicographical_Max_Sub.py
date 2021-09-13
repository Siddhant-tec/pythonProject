alphabets = input()


def LexicographicalMaxString(str):

    answer = ""
    for i in range(len(str)):
        answer = max(mx, str[i:])

    return answer


print(LexicographicalMaxString(alphabets))