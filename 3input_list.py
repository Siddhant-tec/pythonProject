rows = int(input("Enter number of rows in the matrix: "))
columns = int(input("Enter number of columns in the matrix: "))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().rstrip().split())))
print(matrix)
for element in matrix[0]:
    print(element)