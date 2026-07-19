

matrixA = [[1, 2],
           [3, 4]]

matrixB = [[5, 6],
           [7, 8]]

product_result = [[0, 0],
                   [0, 0]]

for i in range(len(matrixA)):         
    for j in range(len(matrixB[0])):   
        total = 0
        for k in range(len(matrixB)):  
            total += matrixA[i][k] * matrixB[k][j]
        product_result[i][j] = total

print("Matrix A:", matrixA)
print("Matrix B:", matrixB)
print("Product of matrices:")
for row in product_result:
    print(row)
