class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        for row in range(9):
            seen = set()
            for col in range(9):
                if board[col][row] == ".":
                    continue
                elif board[col][row] in seen:
                    return False
                seen.add(board[col][row])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j 
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
