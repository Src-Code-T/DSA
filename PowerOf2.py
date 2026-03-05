n = int(input("Enter a number: "))

'''
class Solution:
    def isPow2(self, n: int) -> bool:
        c = 0
        while n > 0:
            if n & 1 > 0:
                c += 1
            n //= 2                 # or n >>= 1
        if c == 1:
            return True
        
        return False
'''

class Solution:
    def isPow2(self, n: int) -> bool:
        if n > 0 and n & (n - 1) == 0:
            return True
        
        return False
    
res = Solution()

r = res.isPow2(n)

print(f'{n} is a power of 2: {r}')