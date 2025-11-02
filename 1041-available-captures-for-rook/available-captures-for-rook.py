class Solution:
    def _findRook(self, board: List[List[str]]) -> (int, int):
        rowPos, colPos = None, None
        for row_index, row in enumerate(board):
            if 'R' in row:
                rowPos = row_index
                for col_index, col_value in enumerate(row):
                    if col_value == 'R':
                        colPos = col_index
        return rowPos, colPos
    
    def _verifyCell(self, board: List[List[str]], row, col) -> bool:
        print("cell")
        print(row, col)
        print(board[row][col])
        if board[row][col] == ".":
            return False
            # continue
        elif board[row][col] == "B":
            return False
        elif board[row][col] == "p":
            return True
        else:
            return False
        

    def _upward(self, board: List[List[str]], rookPos) -> bool:
        print("upward")
        row, col = rookPos[0], rookPos[1]
        res = False
        while row > 0:
            row = row - 1
            if board[row][col] == ".":
                # return False
                continue
            elif board[row][col] == "B":
                return False
            elif board[row][col] == "p":
                return True
            # res = self._verifyCell(board, row, col)
            # print(res)
            # if res:
            #     return True
            #     break
            # if not res:
            #     return False
            #     break


            # if board[row][col] == ".":
            #     continue
            # elif board[row][col] == "B":
            #     return False
            # elif board[row][col] == "p":
            #     return True
            
        return False
    
    def _downward(self, board: List[List[str]], rookPos) -> bool:
        print("downward")
        row, col = rookPos[0], rookPos[1]
        res = False
        while row < 7:
            row = row + 1
            # res = self._verifyCell(board, row, col)
            # if res:
            #     return True
            if board[row][col] == ".":
                # return False
                continue
            elif board[row][col] == "B":
                return False
            elif board[row][col] == "p":
                return True
        return False

    def _forward(self, board: List[List[str]], rookPos) -> bool:
        print("forward")
        row, col = rookPos[0], rookPos[1]
        res = False
        while col < 7:
            col = col + 1
            # res = self._verifyCell(board, row, col)
            # if res:
            #     return True

            if board[row][col] == ".":
                # return False
                continue
            elif board[row][col] == "B":
                return False
            elif board[row][col] == "p":
                return True

        return False
    
    def _backward(self, board: List[List[str]], rookPos) -> bool:
        print("backward")
        row, col = rookPos[0], rookPos[1]
        res = False
        while col > 0:
            col = col - 1
            # res = self._verifyCell(board, row, col)
            # if res:
            #     return True
            if board[row][col] == ".":
                # return False
                continue
            elif board[row][col] == "B":
                return False
            elif board[row][col] == "p":
                return True
        return False

    def numRookCaptures(self, board: List[List[str]]) -> int:
        row, col = self._findRook(board)
        print(row, col)
        up = self._upward(board, rookPos=[row, col])
        down = self._downward(board, rookPos=[row, col])
        forward = self._forward(board, rookPos=[row, col])
        backward = self._backward(board, rookPos=[row, col])

        print(up, down, forward, backward)
        res = up + down + forward + backward

        return res # sum(up, down, forward, backward)

        


        # We have 2D array.
        # in that 2D array we have to first find the Rook representing with R.
        # and find its location in 2D matrix
        # Once found we have to move in four directions on board/2D array.
        # and found pawn represented as p in 2D board.
        # if we 


        # Grid 7x7 : RxC
        # Rook is at 4x4
        # found rook
        # forward:  Rx(C+1)
        # backward: Rx(C-1)
        # Upward:   (R-1)xC
        # Downward: (R+1)xC