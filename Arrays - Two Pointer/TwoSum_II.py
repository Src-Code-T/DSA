class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        n = numbers
        t = target

        while l < r:
            curr_sum = n[l] + n[r]

            if curr_sum == t:
                return [l+1, r+1]

            elif curr_sum < t:
                l += 1

            else:
                r -= 1
