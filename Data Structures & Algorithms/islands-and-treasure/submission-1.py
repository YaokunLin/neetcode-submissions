class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
       
        def bfs(r, c):
            visited = set()
            q = deque([(r, c)])
            steps = 0
            visited.add((r, c))
            while q:
               
                for _ in range(len(q)):
                    cur_r, cur_c = q.popleft()
                    if grid[cur_r][cur_c] == 0:
                        return steps 
                    for dr, dc in directions:
                        nr, nc = cur_r + dr, cur_c + dc
                        if (nr, nc) in visited:
                            continue
                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == -1:
                            continue
                        q.append((nr, nc))
                        visited.add((nr, nc))
                steps += 1
            return INF

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    distance = bfs(i, j)
                    grid[i][j] = distance

        