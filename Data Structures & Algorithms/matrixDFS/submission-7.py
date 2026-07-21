class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1: return 0
        N_ROWS = len(grid)
        N_COLS = len(grid[0])
        if N_ROWS == 1 and N_COLS == 1: return 1
        visited = set([(0, 0)])

        stack = [(0, 0, visited)]
        ds = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        res = 0

        while stack:
            cur_x, cur_y, cur_visited = stack.pop()
            for dx, dy in ds:
                nxt_x, nxt_y = cur_x + dx, cur_y + dy
                if nxt_x < 0: continue
                if nxt_y < 0: continue

                if nxt_x > N_ROWS - 1: continue
                if nxt_y > N_COLS - 1: continue

                if (nxt_x, nxt_y) in cur_visited: continue
                if grid[nxt_x][nxt_y] == 1: continue

                if nxt_x == N_ROWS - 1 and nxt_y == N_COLS - 1: 
                    res += 1
                    continue
                
                nxt_visited = cur_visited.copy()
                nxt_visited.add((nxt_x, nxt_y))
                stack.append([nxt_x, nxt_y, nxt_visited])
        
        return res


                

