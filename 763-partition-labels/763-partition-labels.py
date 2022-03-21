# mrasimzahid.github.io

# Time: O(n)
# Space: O(n)

# Technique: Map_max_prev

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {}
        for index, char in enumerate(s):
            cache[char] = index
        max_, prev, result = 0, -1, []

        for index, char in enumerate(s):
            max_ = max(max_, cache.get(char))
            if max_ == index:
                result.append(max_ - prev)
                prev = max_

        return result