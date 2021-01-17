#https://leetcode.com/problems/count-sorted-vowel-strings/
#https://github.com/MrAsimZahid/LeetCode
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n+4,4)
        
