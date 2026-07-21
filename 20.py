

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 9],
           [1, 2, 3]]

rows = len(matrix1)
cols = len(matrix1[0])

sum_result = []
for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(matrix1[i][j] + matrix2[i][j])
    sum_result.append(new_row)

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Sum of matrices:")
for row in sum_result:
    print(row)
