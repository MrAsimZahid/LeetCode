from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums).most_common(1)
        return count[0][0]