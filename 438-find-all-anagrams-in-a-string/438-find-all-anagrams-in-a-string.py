# mrasimzahid.github.io

# Time: O(n)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        index_list = []
        s_len = len(s)
        p_len = len(p)
        p_count = Counter(p)
        if s is p:
            return [0]
        # sort_p = sorted(p)
        for i in range(s_len-p_len+1):
            if Counter(s[i:p_len+i]) == p_count:
                index_list.append(i)  
        return index_list