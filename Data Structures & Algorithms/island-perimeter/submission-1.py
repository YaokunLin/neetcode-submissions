from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = deque([])
        visited = set([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    stack.append((r, c))
                    visited.add((r, c))
                    break 
        
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        res = 0
        while stack:
            curr_r, curr_c = stack.pop()
            curr_peri_contribute = curr_r - 1 < 0 or grid[curr_r - 1][curr_c] == 0
            curr_peri_contribute += curr_c - 1 < 0 or grid[curr_r][curr_c - 1] == 0
            curr_peri_contribute += curr_r + 1 > len(grid) - 1 or grid[curr_r + 1][curr_c] == 0
            curr_peri_contribute += curr_c + 1 > len(grid[0]) - 1 or grid[curr_r][curr_c + 1] == 0
            res += curr_peri_contribute

            for dir_r, dir_c in dirs:
                nxt_r, nxt_c = curr_r + dir_r, curr_c + dir_c
                if (nxt_r, nxt_c) in visited: 
                    continue
                if nxt_r < 0 or nxt_r > len(grid) - 1:
                    continue
                if nxt_c < 0 or nxt_c > len(grid[0]) - 1:
                    continue
                if grid[nxt_r][nxt_c] == 0:
                    continue
                stack.append((nxt_r, nxt_c))
                visited.add((nxt_r, nxt_c))
        return res



        