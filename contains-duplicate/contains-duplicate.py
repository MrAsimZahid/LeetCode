#https://leetcode.com/problems/contains-duplicate/
#https://github.com/MrAsimZahid
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
