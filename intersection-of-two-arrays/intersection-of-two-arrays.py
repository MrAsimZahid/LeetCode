#https://leetcode.com/problems/intersection-of-two-arrays/
#https://github.com/MrAsimZahid/LeetCode
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))
