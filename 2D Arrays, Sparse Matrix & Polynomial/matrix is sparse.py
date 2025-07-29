def is_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    zero_count = 0
    total = rows * cols

    for row in matrix:
        for val in row:
            if val == 0:
                zero_count += 1

    return zero_count > total // 2

mat = [
    [0, 0, 3],
    [0, 0, 0],
    [0, 4, 0]
]

print("Sparse Matrix" if is_sparse(mat) else "Not a Sparse Matrix")
