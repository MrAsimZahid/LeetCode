# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for index in range(n+1):
            res.append(Counter(bin(index)[2:])['1'])
        return res