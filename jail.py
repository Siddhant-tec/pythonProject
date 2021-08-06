n = int(input())
m = int(input())
s = int(input())

def saveThePrisioner():
    if (m + s - 1) % n == 0:
        return n
    else:
        return (m + s + 1) % n

print(saveThePrisioner())