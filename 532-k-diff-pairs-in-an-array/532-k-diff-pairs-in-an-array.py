# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_count = Counter(nums)
        result = 0
        for num in nums_count:
            if k + num in nums_count and k > 0 or nums_count[num] > 1 and k == 0:
                result += 1
        return result
        