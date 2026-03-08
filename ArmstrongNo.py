class Solution:
    def armstrongNumber (self, n):
        sum = 0
        temp = n
        while temp>0:
            digit = temp % 10
            sum += digit**3
            temp //= 10
            
        if sum == n:
            return True
        return False