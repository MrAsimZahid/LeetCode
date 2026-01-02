class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_map = {}
        for val in nums:
            if val in num_map:
                return val
            num_map[val] = 1
