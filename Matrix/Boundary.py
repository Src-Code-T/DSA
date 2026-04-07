class Solution:
    def boundaryTraversal(self,mat):
        n, m = len(mat), len(mat[0])
        res = []
        
        if n == 1:
            return mat[0]
            
        if m == 1:
            return [mat[i][0] for i in range(n)]
        
        for j in range(m):
            res.append(mat[0][j])
            
        for i in range(1, n):
            res.append(mat[i][m-1])
            
        for j in range(m-2, -1, -1):
            res.append(mat[n-1][j])
            
        for i in range(n-2, 0, -1):
            res.append(mat[i][0])
            
        return res
    
# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
solution = Solution()
print("Boundary Traversal:")
print(solution.boundaryTraversal(matrix))