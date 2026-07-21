class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r, c): 
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '0'
            count = 1
            
            while queue: 
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        count += 1
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            print('count', count)
            return count
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(max_area, area)
               
        return max_area
        

        
        