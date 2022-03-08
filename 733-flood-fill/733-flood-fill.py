# mrasimzahid.github.io

# Graph problem
# Technique: Seek neighbour, depth first search

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc]
        
        def dfs(row, col):
            nonlocal rows, cols, newColor, image
            
            if row < 0 or col < 0 or row > rows-1 or col > cols-1 or image[row][col] == newColor or image[row][col] != color:
                return
            
            image[row][col] = newColor
            
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row-1, col)
            
            
        dfs(sr, sc)
        return image