# mrasimzahid.github.io

# Time: O(n)
# Space: O(1)

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while startValue < target:
            count += 1
            if target % 2:
                target += 1
            else: 
                target //= 2
        return startValue - target + count
        