class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ST = {}
        TS = {}

        for c1, c2 in zip(s, t):

            if c1 in ST:
                if ST[c1] != c2:
                    return False
            else:
                ST[c1] = c2

            if c2 in TS:
                if TS[c2] != c1:
                    return False
            else:
                TS[c2] = c1
        
        return True
            
