# mrasimzahid.github.io

# Technique: DP
# Need to revisit this problem and learn DP properly.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(index, path):
            if sum(path) == target:
                result.append(path[:])
                return
            
            if sum(path) > target:
                return
            
            for x in range(index, len(candidates)):
                path.append(candidates[x])
                helper(x, path)
                path.pop()
        
        helper(0, [])
        return result