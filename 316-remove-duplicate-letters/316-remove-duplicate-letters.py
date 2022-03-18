# mrasimzahid.github.io

# Time: O(n^2)
# Space: O(n)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        stack = []
        
        for i in range(len(s)):
            last_occur[s[i]] = i
            
        for i in range(len(s)):
            if s[i] not in stack:
                while (stack and stack[-1] > s[i] and last_occur[stack[-1]] > i):
                    stack.pop()
                
                stack.append(s[i])
        
        return "".join(stack)
    