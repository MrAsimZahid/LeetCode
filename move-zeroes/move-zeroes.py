#https://leetcode.com/problems/move-zeroes/
#https://github.com/MrAsimZahid
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            if i-1 >= 0 and nums[i-1] == 0:
                nums.pop(i-1)
                nums.append(0)
