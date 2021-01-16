#https://leetcode.com/problems/kth-largest-element-in-an-array/
#https://github.com/MrAsimZahid
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]
