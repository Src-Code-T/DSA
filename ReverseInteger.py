#---45ms--19.3mb---
class Solution:
    def reverse(self, x: int) -> int:
        i_min, i_max = -2**31, 2**31-1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        
        rev *= sign

        if rev < i_min or rev > i_max:
            return 0

        return rev
    
'''
----47ms 18.1mb----
class Solution:
    def reverse(self, x: int) -> int:
        i_min, i_max = -2**31, 2**31-1

        sign = -1 if x < 0 else 1
        x = str(abs(x))

        rev = int(x[::-1])
        
        rev *= sign

        if rev < i_min or rev > i_max:
            return 0

        return rev
'''