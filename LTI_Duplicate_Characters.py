characters = str(input())
answer = list()
for alphabet in characters:
    if alphabet not in answer:
        answer.append(alphabet)
print(''.join(answer))


