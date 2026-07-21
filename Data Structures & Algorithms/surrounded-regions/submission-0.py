class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def explore(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c - 1)
            explore(r, c + 1)

        for i in range(rows):
            if board[i][0] == 'O':
                explore(i, 0)
            if board[i][cols - 1] == 'O':
                explore(i, cols - 1)
        for j in range(cols):
            if board[0][j] == 'O':
                explore(0, j)
            if board[rows - 1][j] == "O":
                explore(rows - 1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        
            
  