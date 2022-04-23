# mrasimzahid.github.io


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
            
        for i in range(1, n + 1):
            if trusted[i] == n-1:
                return i
        return -1
        
        
        
        
        
        
#         everybody -> town_judge
#         town_judge x-> anyone
        
        
        
        
        
        
        
        
        
#         {
#             1: 2,
#             3: 3,
#             2: 1,

#         }
#         temp = 0
        