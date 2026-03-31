class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt = Counter(magazine)

        for s in ransomNote:
            if cnt[s] == 0:
                return False
            cnt[s] -= 1

        return True
        