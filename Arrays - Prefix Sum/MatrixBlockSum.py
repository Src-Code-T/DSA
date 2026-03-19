
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        p = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                p[i][j] = (
                    mat[i-1][j-1]
                    + p[i-1][j]
                    + p[i][j-1]
                    - p[i-1][j-1]
                )

        res = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(0, i-k)
                c1 = max(0, j-k)
                r2 = min(n-1, i+k)
                c2 = min(m-1, j+k)

                res[i][j] = (
                    p[r2+1][c2+1]
                    - p[r1][c2+1]
                    - p[r2+1][c1]
                    + p[r1][c1]
                )

        return res
    