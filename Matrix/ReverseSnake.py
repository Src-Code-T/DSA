def snake_row_reverse(matrix):
    res = []
    for i in range(len(matrix)):
        if i % 2 == 0:
            for j in range(len(matrix[0]) - 1, -1, -1):
                res.append(matrix[i][j])
        else:
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
    return res

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Reverse Snake Pattern Row Wise:")
print(snake_row_reverse(matrix))


def snake_col_reverse(matrix):
    res = []
    rows, cols = len(matrix), len(matrix[0])
    
    for j in range(cols):
        if j % 2 == 0:
            for i in range(rows - 1, -1, -1):
                res.append(matrix[i][j])
        else:
            for i in range(rows):
                res.append(matrix[i][j])
    return res

# Example usage:
print("\nReverse Snake Pattern Column Wise:")
print(snake_col_reverse(matrix))