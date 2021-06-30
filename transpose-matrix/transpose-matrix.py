class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Transpose matrix: another methos numpy.transpose(matrix)
        rotate 90 degree by [*zip(*matrix)][::-1]        
        """
        return [*zip(*matrix)]
        