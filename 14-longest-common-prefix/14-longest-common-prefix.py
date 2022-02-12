# mrasimzahid.github.io

# Time: O(n)
# Space: O(n)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_list = list(zip(*strs))
        prefix = ""
        for char in str_list:
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break
        return prefix