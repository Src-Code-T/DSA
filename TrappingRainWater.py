class Solution:
    def maxWater(self, arr):
        l = 0
        r = len(arr)-1
        l_max = 0
        r_max = 0
        res = 0
        
        while l < r:
            if arr[l] < arr [r]:
                if arr[l] >= l_max:
                    l_max = arr[l]
                else:
                    res += l_max - arr[l]
                    
                l += 1
            else:
                if arr[r] >= r_max:
                    r_max = arr[r]
                else:
                    res += r_max - arr[r]
                
                r -= 1
            
                
                
        return res
                
