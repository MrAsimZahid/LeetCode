# mrasimzahid.github.io

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cache = []
        for index, row in enumerate(mat):
            cache.append([sum(row), index])
        cache.sort()
        return [score[1] for score in cache[:k]]