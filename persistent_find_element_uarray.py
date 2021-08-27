size = int(input())
numbers = list()
for elements in range(size):
    element = int(input())
    numbers.append(element)
number = int(input())
if number in numbers:
    print("YES")
else:
    print("NO")