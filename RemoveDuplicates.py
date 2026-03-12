class Solution:
    def removeDuplicates(self, arr):
        s = set()
        res = []
        
        for x in arr:
            if x not in s:
                s.add(x)
                res.append(x)
        
        return res
    
