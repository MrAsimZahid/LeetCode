# mrasimzahid.github.io

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        t = s
        index_pop = []
        stack = []
        for index, value in enumerate(t):
            if value == "(":
                stack.append((value, index))
            elif value == ")":
                if stack:
                    if stack[-1][0] == "(":
                        stack.pop()
                    else:
                        index_pop.append(index)
                else:
                    index_pop.append(index)
        for each in stack:
            index_pop.append(each[1])
        sort_index = index_pop.sort()
        s = list(s)
        if index_pop:
            for each in index_pop[::-1]:
                s.pop(each)
        return s