#https://leetcode.com/problems/uncommon-words-from-two-sentences/
#https://github.com/MrAsimZahid/LeetCode
from collections import Counter
class Solution:
    """
    k: key
    v: value
    """
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [k for k, v in collections.Counter(A.split() + B.split()).items() if v == 1 ]
        """
        s = A + " " + B
        #return s.split()
        word_freq = dict(Counter(s.split()))
        word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=False)
        #return word_freq
        return [word_freq[[0][i]] for i, v in enumerate(word_freq) if v == 1]
    #list(word_freq.keys())[list(word_freq.values()).index(1)]
        """
