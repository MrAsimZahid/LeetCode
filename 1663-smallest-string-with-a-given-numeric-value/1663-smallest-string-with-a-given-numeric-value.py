# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        print(k)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = 'z' * (k//25)
        if (k % 25):
            res = alphabet[k % 25] + res
        return 'a' * (n - len(res)) + res
    