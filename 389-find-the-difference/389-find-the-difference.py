# mrasimzahid.github.io

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # solution 1
        # Time: O(n)
        # Space: O(n)
        s_counter = Counter(s)
        t_counter = Counter(t)
        for i in set(t):
            if s_counter[i] < t_counter[i]:
                return i

        # Time: O(n)
        # Space: O(1)
#         # solution 2
#         total = 0
#         for char in t:
#             total += ord(char)
#         for char in s:
#             total -= ord(char)
#         return chr(total)
        