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
