
class Solution:
    def count(self, N):
        if N<=2:
            return 1
        
        tot = 0
        for i in range(0, N, 2):
            tot += self.count(i) * self.count(N-2-i)
            
        return tot
    
