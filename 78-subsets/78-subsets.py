# mrasimzahid.github.io

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            subset += [s_set+[num] for s_set in subset]
        return subset