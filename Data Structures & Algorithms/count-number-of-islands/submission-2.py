class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        count = 0
        def explore(r, c):
            if r >= row or c >= col or r < 0 or c < 0:
                return
            if grid[r][c] == "0":
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c - 1)
            explore(r, c + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    explore(i, j)
        return count

           
       
      


        
     




        