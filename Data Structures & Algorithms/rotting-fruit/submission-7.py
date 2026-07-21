class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        while fresh > 0 and q:
            len_q = len(q)
            for i in range(len_q):
                r, c = q.popleft()
                for direction in directions:
                    cur_row = r + direction[0]
                    cur_col = c + direction[1]
                    if 0 <= cur_row < rows and 0 <= cur_col < cols and grid[cur_row][cur_col] == 1:
                        grid[cur_row][cur_col] = 2
                        fresh -= 1
                        q.append((cur_row, cur_col))
            time += 1
        if fresh == 0:
            return time
        else:
            return -1
            


   


        