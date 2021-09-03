numbers = list(map(int, input().rstrip().split()))
numbers2 = list(map(int, input().rstrip().split()))


def remove_duplicate(numbers):
    dup = []
    for element in numbers:
        if element not in dup:
            dup.append(element)
    return dup


final = sorted(remove_duplicate(numbers) + remove_duplicate(numbers2))
print(final)
index = len(final) // 2
print(final[index])
print(final[index + 1])
result = (final[index] + final[~index])/2
print(result)


