class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        N_ROWS = len(grid)
        N_COLS = len(grid[0])

        # Edge case: If start is blocked
        if grid[0][0] == 1:
            return 0

        # Initialize the stack with (0,0) ALREADY in the visited set
        visited = {(0, 0)}
        stack = [(0, 0, visited)]
        n_paths = 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while stack:
            # Note: pop() is DFS (faster path finding), pop(0) is BFS. 
            # pop() is generally better here to keep memory lower.
            cur_r, cur_c, cur_visited = stack.pop()

            # Check for destination right when we pop it, catching 1x1 grids
            if cur_r == N_ROWS - 1 and cur_c == N_COLS - 1:
                n_paths += 1
                continue

            for dir_r, dir_c in dirs:
                nxt_r, nxt_c = cur_r + dir_r, cur_c + dir_c
                
                # Correct boundary checks (>= instead of >)
                if nxt_r < 0 or nxt_r >= N_ROWS: continue
                if nxt_c < 0 or nxt_c >= N_COLS: continue

                # Check for rocks and visited cells
                if grid[nxt_r][nxt_c] == 1: continue
                if (nxt_r, nxt_c) in cur_visited: continue
                
                # CRITICAL FIX: Copy the set BEFORE modifying it 
                # so other directions in this loop aren't affected
                nxt_visited = cur_visited.copy()
                nxt_visited.add((nxt_r, nxt_c))
                
                stack.append((nxt_r, nxt_c, nxt_visited))
                
        return n_paths