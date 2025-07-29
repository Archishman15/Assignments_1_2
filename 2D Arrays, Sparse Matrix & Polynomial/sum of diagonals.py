def sum_of_diagonals(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n - i - 1]
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    return total

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Sum of diagonals:", sum_of_diagonals(mat))
