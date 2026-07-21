from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        N_ROWS = len(grid)
        N_COLS = len(grid[0])
        
        # Edge case: blocked start or end
        if grid[0][0] == 1 or grid[N_ROWS - 1][N_COLS - 1] == 1:
            return -1
            
        if N_ROWS == 1 and N_COLS == 1: return 0

        # Mark the start node visited IMMEDIATELY
        visited = set()
        visited.add((0, 0)) 
        
        dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        q = deque([(0, 0, 0)])
        
        while q:
            cur_row, cur_col, cur_distance = q.popleft()
            
            # (Notice visited.add is no longer here)
            
            if cur_row == N_ROWS - 1 and cur_col == N_COLS - 1: 
                return cur_distance

            for dir_x, dir_y in dirs:
                nxt_row, nxt_col = cur_row + dir_x, cur_col + dir_y
                
                # Check boundaries and obstacles
                if 0 <= nxt_row < N_ROWS and 0 <= nxt_col < N_COLS and grid[nxt_row][nxt_col] == 0:
                    # Check visited
                    if (nxt_row, nxt_col) not in visited:
                        # THE FIX: Mark visited right BEFORE appending
                        visited.add((nxt_row, nxt_col))
                        q.append((nxt_row, nxt_col, cur_distance + 1))
        
        return -1