rows = int(input())
columns = int(input())
matrix = list()
r = list()
c = list()
for i in range(rows):
    matrix.append(list(map(int, input().split())))

print(matrix)

for i in range(rows):
    row_sum = 0
    for j in range(columns):
        row_sum += matrix[i][j]
    r.append(row_sum)

for i in range(rows):
    col_sum = 0
    for j in range(columns):
        col_sum += matrix[j][i]
    c.append(col_sum)

print(max(r), max(c))
