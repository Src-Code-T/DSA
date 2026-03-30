class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        l, max_len = 0, 0

        for r in range(len(fruits)):
            cnt[fruits[r]] += 1

            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0:
                    del cnt[fruits[l]]
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
