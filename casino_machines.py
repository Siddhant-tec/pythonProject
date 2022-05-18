rubles = int(input())
A = int(input())
B = int(input())
C = int(input())
count = 0

while rubles > 0:
    A += 1
    rubles -= 1
    count += 1
    if A == 25:
        rubles += 20
        A = 0

    B += 1
    rubles -= 1
    count += 1
    if B == 120:
        rubles += 80
        B = 0

    C += 1
    rubles -= 1
    count += 1
    if C == 12:
        rubles += 8
        C = 0

print(count - 1)
