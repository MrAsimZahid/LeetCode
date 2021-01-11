#https://leetcode.com/problems/squares-of-a-sorted-array/
#https://github.com/MrAsimZahid
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
