#https://leetcode.com/problems/kth-largest-element-in-an-array/
#https://github.com/MrAsimZahid
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
