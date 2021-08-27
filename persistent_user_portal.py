n = int(input())
users = list()
answer = list()
for people in range(n):
    person = input()
    if person in users:
        count = users.count(person)
        answer.append(person+str(count))
        users.append(person)

    else:
        users.append(person)
        answer.append(person)




print(answer)
