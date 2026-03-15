class Solution:
    def majorityElement(self, arr):
        
        n = len(arr)
        cnt = 0
        cand = 0
        
        
        for i in range(n):
            if cnt == 0:
                cand = arr[i]
                cnt = 1
            else:
                if cand == arr[i]:
                    cnt += 1
                else:
                    cnt -= 1
                    
        cnt = 0
        
        for i in range(n):
            if cand == arr[i]:
                cnt += 1
                
        if 2*cnt > n:
            return cand
            
        return -1
