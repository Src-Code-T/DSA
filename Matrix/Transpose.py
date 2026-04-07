class Solution:
    def transpose(self, mat):
        n, m = len(mat), len(mat[0])
        
        tmat = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
                tmat[i][j] = mat[j][i]
                
        return tmat
    
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution = Solution()
print("Transposed Matrix:")
print(solution.transpose(matrix))

