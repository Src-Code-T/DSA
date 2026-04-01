class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        mapCW = {}
        mapWC = {}

        for c, w in zip(pattern, words):

            if c in mapCW:
                if mapCW[c] != w:
                    return False
            else:
                mapCW[c] = w

            if w in mapWC:
                if mapWC[w] != c:
                    return False
            else:
                mapWC[w] = c

        return True
        