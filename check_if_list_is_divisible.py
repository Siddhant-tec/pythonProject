myList = list(map(int, input().rstrip().split()))
myInt = int(input())
answer = []

for x in myList:
    answer.append(x % myInt)

if answer.count(0) == len(myList):
    print("T")
else:
    print("F")


print(answer)