class Solution:
    def isPalindrome(self, x: int) -> bool:
        n1 = 0
        m = x

        if x < 0 :
            return False

        while m > 0:
            n1 = n1*10 + (m%10)
            m = m//10

        if n1 == x:
            return True
        else:
            return False