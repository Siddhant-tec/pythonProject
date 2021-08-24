encode = input()
decode = input()

encoded = list()
decoded = list()

for values in encode:
    encoded.append(chr((ord(values))+5))

for values2 in decode:
    decoded.append(chr((ord(values2))-5))


print(''.join(encoded))
print(''.join(decoded))
