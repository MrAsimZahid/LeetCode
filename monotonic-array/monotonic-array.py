#https://leetcode.com/problems/monotonic-array/
#https://github.com/MrAsimZahid
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A)[::-1]
