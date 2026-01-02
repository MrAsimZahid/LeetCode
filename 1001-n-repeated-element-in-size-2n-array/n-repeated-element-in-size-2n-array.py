from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_half_len = floor(len(nums)/2) 
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] in nums_map:
                nums_map[nums[i]] = nums_map[nums[i]] + 1
                if nums_map[nums[i]] >= nums_half_len:
                    return nums[i]
            else:
                nums_map[nums[i]] = 1