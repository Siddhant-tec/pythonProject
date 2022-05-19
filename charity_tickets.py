pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())

p = total // pink
g = total // green
r = total // red
o = total // orange
count = 0
ls = []

for i in range(p + 1):
    for j in range(g + 1):
        for k in range(r + 1):
            for l in range(o + 1):
                if (i * pink) + (j * green) + (k * red) + (l * orange) == total:
                    count += 1
                    print("# of Pink is", i, "# of green is", j, "# of red is", k, "# of orange is", l)
                    x = i + j + k + l
                    ls.append(x)

print("Total Combinations: " + str(count))
print("Minimum number of tickets is", min(ls))
