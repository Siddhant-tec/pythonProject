rows = int(input("Enter number of rows in the matrix: "))
columns = int(input("Enter number of columns in the matrix: "))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))
print(matrix)
for element in matrix[0]:
    print(element)

x = [sum(x) for x in zip(*matrix)]
print(x)

matrix2 = [[3, 4], [5, 6]]
result = [list(map(sum, zip(*t))) for t in zip(matrix, matrix2)]
print(result)
print(matrix + matrix2)