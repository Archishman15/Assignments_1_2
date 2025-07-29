class RotateMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def rotate_90_clockwise(self):
        for i in range(self.n):
            for j in range(i, self.n):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        for i in range(self.n):
            self.matrix[i].reverse()

    def print_matrix(self):
        for row in self.matrix:
            print(*row)

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotator = RotateMatrix(mat)
rotator.rotate_90_clockwise()
rotator.print_matrix()
