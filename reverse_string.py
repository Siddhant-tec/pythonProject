l = list(map(int, input().rstrip().split()))

for i in range(len(l)//2):
    temp = l[i]
    l[i] = l[-i - 1]
    l[-i - 1] = temp

print(l)

