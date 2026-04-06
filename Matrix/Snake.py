class Solution:
    def snakePattern(self, matrix):
        if not matrix:
            return []
            
        r, c = len(matrix), len(matrix[0])
        res = []
        
        for i in range(r):
            
            if i % 2 == 0:
                for j in range(c):
                    res.append(matrix[i][j])
                    
            else:
                for j in range(c-1, -1, -1):
                    res.append(matrix[i][j])
                    
        return res
    
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print("Snake Pattern Row Wise:")
solution = Solution()
print(solution.snakePattern(matrix))

#Snake Column Wise
def snake_column(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    for j in range(cols):
        if j % 2 == 0:
            for i in range(rows):
                print(matrix[i][j])
        else:
            for i in range(rows - 1, -1, -1):
                print(matrix[i][j])

# Example usage:
print("\nSnake Pattern Column Wise:")
snake_column(matrix)
