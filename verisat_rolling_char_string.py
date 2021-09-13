alphabets = list(input())
roll = list(input())
answer = list()
for i in range(len(roll)):
    for character in range(len(alphabets)):
        while character <= int(roll[i]):
            x = chr(ord(alphabets[character]) + int(roll[i]))
            answer.append(x)
            break
        continue

print(answer)
