class Solution:
    def leaders(self, arr):
        n = len(arr)
        res = []
        max_ele = arr[-1]
        
        if n == 1:
            return arr
            
        for i in range(n-1, -1, -1):
            if arr[i] >= max_ele:
                res.append(arr[i])
                max_ele = arr[i]
                
        return res[::-1]
    
