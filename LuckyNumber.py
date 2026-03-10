class Solution:
    cntr = 2
    
    def isLucky(self, n):
        if self.cntr > n:
            return 1
        if n % self.cntr == 0:
            return 0
        n = n-(n//self.cntr)
        
        self.cntr += 1
        
        return self.isLucky(n)