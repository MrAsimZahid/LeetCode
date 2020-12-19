#https://leetcode.com/problems/single-number/
#https://github.com/MrAsimZahid
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda kv: kv[1])[0][0]
