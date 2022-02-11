# mrasimzahid.github.io

# similar to find all anagrams

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        len_s1 = len(s1)
        for i in range(len(s2)):
            if s1_count == Counter(s2[i:i+len_s1]):
                return True
        return False