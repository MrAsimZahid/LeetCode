#https://leetcode.com/problems/find-the-duplicate-number/
#https://github.com/MrAsimZahid
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
