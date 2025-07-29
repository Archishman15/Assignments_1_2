def count_zeros(matrix):
    count = 0
    for row in matrix:
        for val in row:
            if val == 0:
                count += 1
    return count

mat = [
    [0, 1, 2],
    [3, 0, 4],
    [0, 5, 0]
]

print("Zero count:", count_zeros(mat))
