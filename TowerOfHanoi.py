class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n == 1:
            return 1
        return 2*self.towerOfHanoi(n-1, fromm, aux, to) + 1
