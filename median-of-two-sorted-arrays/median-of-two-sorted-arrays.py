from statistics import median
#https://leetcode.com/problems/median-of-two-sorted-arrays/
#https://github.com/MrAsimZahid
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1 + nums2
        return median(x)
