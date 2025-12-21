from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        deleted = 0
        sorted_pairs = [False] * (n - 1)
        
        for c in range(m):
            # Check if this column breaks ordering
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            
            if bad:
                deleted += 1
                continue
            
            # Update sorted_pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] < strs[i + 1][c]:
                    sorted_pairs[i] = True
        
        return deleted
