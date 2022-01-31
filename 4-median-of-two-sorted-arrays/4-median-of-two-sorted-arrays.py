class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_ = len(nums1 + nums2)
        if len_ % 2 == 0:
            sor = sorted(nums1+nums2)
            i = len(nums1 + nums2)//2
            return (sor[i] +sor[i-1])/2
        else:
            sor = sorted(nums1+nums2)
            return sor[len(nums1 + nums2)//2]