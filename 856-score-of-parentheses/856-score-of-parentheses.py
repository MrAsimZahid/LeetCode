# mrasimzahid.github.io

# Time: O(n)
# Space: O(n)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                num = stack.pop()
                stack[-1] += 1 if num == 0 else 2*num
        return stack[0]
        