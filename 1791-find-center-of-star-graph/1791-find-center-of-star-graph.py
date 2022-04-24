# mrasimzahid.github.io

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Solution 1
        # edge = edges[0] + edges[1]
        # res = collections.Counter(edge)
        # return res.most_common()[0][0]
        
        # Solution 2
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
