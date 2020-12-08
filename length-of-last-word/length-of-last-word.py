#https://leetcode.com/problems/length-of-last-word/
#https://github.com/MrAsimZahid
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        #Solution 1
        count = 0
        for index in range(len(s)-1, 0-1, -1): # s[::-1]:
            if s[index] != " ":
                count += 1
            if s[index] == " ":
                break
        return count
    """
        # solution 2
        """
        count = 0
        for element in s[::-1]:
            if s[index] != " ":
                count += 1
            if s[index] == " ":
                break
        return count
        """
        #Solution3
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
