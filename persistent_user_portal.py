users = list(map(str, input().rstrip().split()))
freq = dict()
for people in users:

    if people in freq:
        freq[people] += 1

    else:
        freq[people] = 1


print(freq)
print(users)
