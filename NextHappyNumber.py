
class Solution:
    def nextHappy (self, N):
        
        def Happy(x):
            seen = set()
            
            while x != 1 and x not in seen:
                seen.add(x)
                x = sum(int(d)**2 for d in str(x))
                
            return x == 1
            
        n = N + 1
        
        while not Happy(n):
            n += 1
            
        return n
