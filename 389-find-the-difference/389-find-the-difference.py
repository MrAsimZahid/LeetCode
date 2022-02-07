# mrasimzahid.github.io

# Time: O(n)
# Space: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total = 0
        for char in t:
            total += ord(char)
        for char in s:
            total -= ord(char)
        return chr(total)
        