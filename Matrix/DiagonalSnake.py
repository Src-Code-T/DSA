def diagonal_snake(matrix):
    res = []
    rows, cols = len(matrix), len(matrix[0])
    
    for d in range(rows + cols - 1):
        temp = []
        
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                temp.append(matrix[i][j])
        
        # reverse every alternate diagonal
        if d % 2 == 0:
            temp.reverse()
        
        res.extend(temp)
    
    return res

# Example usage:
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print("Diagonal Snake Pattern:")
print(diagonal_snake(matrix))