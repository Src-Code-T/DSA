class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_map = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in count_map:
                count += count_map[curr_sum - k]

            count_map[curr_sum] = count_map.get(curr_sum, 0) + 1

        return count
    
