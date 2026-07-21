from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        N_ROWS, N_COLS = len(grid), len(grid[0])
        r, c = 0, 0
        q = deque([(r, c, 0)]) # current position, curr_length
        dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        seen = set([(r, c)])

        while q:
            cur_x, cur_y, cur_len = q.popleft()
            if cur_x == N_ROWS - 1 and cur_y == N_COLS - 1: return cur_len
            
            # explore 
            for dir_x, dir_y in dirs: 
                nxt_x, nxt_y = cur_x + dir_x, cur_y + dir_y
                if nxt_x < 0 or nxt_x > N_ROWS - 1: continue
                if nxt_y < 0 or nxt_y > N_COLS - 1: continue
                if (nxt_x, nxt_y) in seen: continue
                if grid[nxt_x][nxt_y] == 1: continue

                seen.add((nxt_x, nxt_y))
                q.append([nxt_x, nxt_y, cur_len + 1])
        
        return -1


        
        