# mrasimzahid.github.io

# Time: O(n^2)
# Sace: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            res = 0
            for each in str(num):
                res += int(each)
            num = res
        return num