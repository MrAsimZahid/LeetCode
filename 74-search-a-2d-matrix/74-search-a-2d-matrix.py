# mrasimzahid.github.io

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
            
        return False