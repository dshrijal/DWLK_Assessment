class  Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = None
    def create_matrix_by_user(self):
        self.matrix = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                value = int(input(f"Enter value for position ({i+1}, {j+1}): "))
                row.append(value)
            self.matrix.append(row)
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        result = Matrix(self.rows, other.cols)
        result.matrix = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result
    def __str__(self):
        if self.matrix is None:
            return "Matrix not created yet."
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])
    