alphabets = list(input())
roll = list(input())
answer = list()
for i in range(len(roll)):
    for character in range(len(alphabets)):
        while character <= int(roll[i]):
            alphabets[character] = chr(ord(alphabets[character]) + 1)
            break
        continue

print(alphabets)
