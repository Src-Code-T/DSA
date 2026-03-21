class Solution:
    def minTime(self, house, d):
        house.sort()
        
        def can_deliver(t):
            n = len(house)
            i = 0
            used = 0
            
            while i < n:
                used += 1
                if used > d:
                    return False
                    
                j = i
                
                while j < n:
                    k = j - i + 1
                    time = 2*k + house[j]
                    
                    if time > t:
                        break
                    j += 1
                    
                i = j
                
            return True
            
        l = 0
        r = 10**15
        ans = r
        
        while l <= r:
            m = (l + r)//2
            
            if can_deliver(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

