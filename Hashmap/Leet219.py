'''
#Sliding Window 38ms 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()

        for i in range(len(nums)):
            if nums[i] in win:
                return True
            
            win.add(nums[i])

            if len(win) > k:
                win.remove(nums[i-k])

        return False
'''
#Hashmap 31ms
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        
        return False
        