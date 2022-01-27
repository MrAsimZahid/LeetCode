# mrasimzahid.github.io

from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])                
        for str in words[1:]:
            common_counter &= Counter(str)                                    
        return list(common_counter.elements())
		