# mrasimzahid.github.io

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge = edges[0] + edges[1]
        res = collections.Counter(edge)
        return res.most_common()[0][0]
