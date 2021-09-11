number = input()
answer = list()
for digit in number:
    if int(digit) % 2 == 0:
        d = int(digit) + 1
        answer.append(str(d))
    else:
        answer.append(digit)

print(answer)
print(''.join(answer))
