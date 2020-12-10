#https://leetcode.com/problems/valid-palindrome/
#https://github.com/MrAsimZahid
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Solution 1
        x = re.sub(r'[^A-Za-z0-9]+', '',s).lower()
        return x == x[::-1]
    #Solution 2
#        return True if re.sub(r'[^\w\s]','',s.lower().replace(" ", "")[::-1]) == #re.sub(r'[^\w\s]','',s.lower().replace(" ", "")) else False
​
