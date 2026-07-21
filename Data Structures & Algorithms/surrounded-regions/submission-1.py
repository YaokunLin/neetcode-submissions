class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
      
        def explore(r, c):
            stack = [(r, c)]
            while stack:
                cur_r, cur_c = stack.pop()
                if cur_r < 0 or cur_c < 0 or cur_r >= rows or cur_c >= cols or board[cur_r][cur_c] != "O":
                    continue 
                
                board[cur_r][cur_c] = "T"
                stack.append((cur_r + 1,cur_c))
                stack.append((cur_r - 1, cur_c))
                stack.append((cur_r, cur_c - 1))
                stack.append((cur_r, cur_c + 1))

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

        
            
  