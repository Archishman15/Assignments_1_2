def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
                return False
    return True

mat = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print("Identity Matrix" if is_identity(mat) else "Not an Identity Matrix")
