# mrasimzahid.github.io

class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while num > 9:
            res = 0
            for each in str(num):
                res += int(each)
            num = res
        return num