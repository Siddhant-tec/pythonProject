s = input("")
answer = []
for element in s:
    if element in answer:
        continue
    else:
        answer.append(element)


print("".join(answer))
print(len(answer))
print(set(s))