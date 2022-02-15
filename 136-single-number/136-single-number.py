# mrasimzahid.github.io

# Time: O(n)
# Space O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result