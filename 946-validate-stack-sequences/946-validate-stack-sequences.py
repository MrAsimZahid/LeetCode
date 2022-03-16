# mrasimzhaid.github.io

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = 0
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[count]:
                count += 1
                stack.pop()
        return len(stack) == 0
        