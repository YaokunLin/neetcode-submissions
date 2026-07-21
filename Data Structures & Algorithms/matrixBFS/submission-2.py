from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        N_ROWS = len(grid)
        N_COLS = len(grid[0])
        if N_ROWS == 1 and N_COLS == 1: return 0

        visited = set()
        dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        q = deque([(0, 0, 0)])
        while q:
            cur_row, cur_col, cur_distance = q.popleft()
            visited.add((cur_row, cur_col))
            if cur_row == N_ROWS - 1 and cur_col == N_COLS - 1: return cur_distance

            for dir_x, dir_y in dirs:
                nxt_row, nxt_col, nxt_distance = cur_row + dir_x, cur_col + dir_y, cur_distance + 1
                if 0 > nxt_row or nxt_row >= N_ROWS: continue
                if 0 > nxt_col or nxt_col >= N_COLS: continue
                if grid[nxt_row][nxt_col] == 1: continue
                if (nxt_row, nxt_col) in visited: continue
                q.append((nxt_row, nxt_col, nxt_distance))
                visited.add((nxt_row, nxt_col))
        
        return -1


        