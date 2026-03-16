class Solution:
    def maxEvenOdd(self,arr):
        n = len(arr)
        res = 1
        cur = 1
        
        for i in range(1, n):
            if arr[i]%2 != arr[i-1]%2:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
                
        return res
            
