# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        col_len = len(columnTitle)
        for index, char in enumerate(columnTitle):
            if index == 0:
                res = ord(char) - 64
            else:
                res = res * 26 + (ord(char) - 64)
        return res