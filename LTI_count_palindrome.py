sentence = str(input())
sentence = sentence.split(" ")

def check_palindrome():
    count = 0
    for word in sentence:
        if word.lower() == word.lower()[::-1]:
            count += 1

    print(count)

check_palindrome()