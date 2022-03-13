# mrasimzahid.github.io

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Using dictionary
        """
        parenth_dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for each in s:
            if each in parenth_dict:
                if stack != [] and parenth_dict[each] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(each)
        if stack == []:
            return True
        else: 
            return False
