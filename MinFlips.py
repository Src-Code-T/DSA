#Minimum Number of Flips to Make the Binary String Alternating
class Solution:
    def minFlips(self, s):
        n = len(s)
        c1 = 0
        c2 = 0
        
        for i in range(n):
            if i%2 == 0 and s[i] == "1":
                c1 += 1
            elif i%2 == 1 and s[i] == '0':
                c1 += 1
                
            if i%2 == 0 and s[i] == "0":
                c2 += 1
            elif i%2 == 1 and s[i] == "1":
                c2 += 1
                
        return min(c1, c2)
        
