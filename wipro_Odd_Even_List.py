numbers = list(map(int, input().rstrip().split()))
even = list()
odd = list()
for element in numbers:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)

print(even)
print(odd)

answer = [None]*(len(even) + len(odd))
answer[::2] = sorted(even)
answer[1::2] = sorted(odd)
print(answer)



## method #2
list3 = []
while True:
    try:
        list3.append(even.pop(0))
        list3.append(odd.pop(0))
    except IndexError:
        break

print(list3)