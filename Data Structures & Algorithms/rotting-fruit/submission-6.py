class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_num = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        elapsed_time = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_num += 1
        while queue:
            row, col, minutes = queue.popleft()
            elapsed_time = max(elapsed_time, minutes)
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, minutes + 1))
                    fresh_num -= 1

        if fresh_num == 0:
  
            return elapsed_time
        else:
            print(fresh_num)
            return -1


        