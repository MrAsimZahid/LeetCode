# mrasimzahid.github.io

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(c.isupper() for c in word)
        return cnt in (len(word), 0, 1 & word[0].isupper())