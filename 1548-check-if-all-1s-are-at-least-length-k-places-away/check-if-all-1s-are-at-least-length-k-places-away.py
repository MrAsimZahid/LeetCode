class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        if 1 not in nums or len(nums) == 0:
            return True
        prev = None
        # subtract index - previous flag <= distance 
        for index, num in enumerate(nums):
            if num == 1:
                if prev is not None and index - prev <= k:
                    return False
                prev = index
        return True
