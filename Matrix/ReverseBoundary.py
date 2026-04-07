def revBoundary(mat):
    n, m = len(mat), len(mat[0])
    res = []

    if n == 1:
        return mat[0][::-1]
    
    if m == 1:
        return [mat[i][0] for i in range(n-1, -1, -1)]
    
    for j in range(m-1, -1, -1):
        res.append(mat[0][j])

    for i in range(1, n):
        res.append(mat[i][0])

    for j in range(1, m):
        res.append(mat[n-1][j])

    for i in range(n-2, 0, -1):
        res.append(mat[i][m-1])

    return res

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Reverse Boundary Traversal:")
print(revBoundary(matrix))
