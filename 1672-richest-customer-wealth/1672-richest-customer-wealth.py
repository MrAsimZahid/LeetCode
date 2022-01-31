# mrasimzahid.github.io

# time: O(n)
# space: O(1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for each in accounts:
            max_sum = max(max_sum, sum(each))
        return max_sum