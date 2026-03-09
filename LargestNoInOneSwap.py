
class Solution:
    def largestSwap(self, s):
        s = list(s)
        last = {d:i for i, d in enumerate(s)}
        
        for i, x in enumerate(s):
            for d in "9876543210":
                if d > x and last.get(d, -1) > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    
                    return "".join(s)
        
        return "".join(s)

