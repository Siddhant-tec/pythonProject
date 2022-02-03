length = int(input())
numbers = list(map(int, input().rstrip().split()))
answer = list()


def divison(myInt, myList):
    newList = [x % myInt for x in myList]
    if newList.count(0) == length:
        return True
    else:
        return False


for number in numbers:
    if number > 0 and divison(number, numbers) is True:
        answer.append(number)

result = 1
for element in answer:
    result *= element

print(result)
print(answer)