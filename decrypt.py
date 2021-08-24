from itertools import repeat
code = list(input())
answer = list()
for i in range(0, len(code)):
    previous = code[i-1]
    if code[i].isdigit():
        answer.extend(repeat(previous, int(code[i])))
print(''.join(answer))
