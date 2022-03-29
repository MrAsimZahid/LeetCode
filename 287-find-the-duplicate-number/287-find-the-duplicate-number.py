# mrasimzahid.github.io

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = {}
        for each in nums:
            if each in cache:
                return each
            else:
                cache[each] = 1