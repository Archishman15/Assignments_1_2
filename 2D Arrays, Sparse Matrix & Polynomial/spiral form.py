class SpiralMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def print_spiral(self):
        top, bottom = 0, self.rows - 1
        left, right = 0, self.cols - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                print(self.matrix[top][i], end=' ')
            top += 1

            for i in range(top, bottom + 1):
                print(self.matrix[i][right], end=' ')
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    print(self.matrix[bottom][i], end=' ')
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    print(self.matrix[i][left], end=' ')
                left += 1

mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

spiral = SpiralMatrix(mat1)
spiral.print_spiral()
