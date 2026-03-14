class Solution:
    def maxOnes(self, arr, k):
        l = 0
        cnt = 0
        max_len = 0
        
        for r in range(len(arr)):
            
            if arr[r] == 0:
                cnt +=1
                
            while cnt > k:
                if arr[l] == 0:
                    cnt -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)
            
        return max_len

