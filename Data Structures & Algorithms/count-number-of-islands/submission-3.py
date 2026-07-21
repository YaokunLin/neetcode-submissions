class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0
        def explore(r, c):
            stack= [(r, c)]
            while stack:
                curr_r, curr_c = stack.pop()
                if curr_r >= rows or curr_c >= cols or curr_r < 0 or curr_c < 0:
                    continue
                if grid[curr_r][curr_c] == "0":
                    continue
                if (curr_r, curr_c) in visited:
                    continue
                visited.add((curr_r, curr_c))
                stack.append((curr_r - 1, curr_c))
                stack.append((curr_r + 1, curr_c))
                stack.append((curr_r, curr_c - 1))
                stack.append((curr_r, curr_c + 1))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    explore(i, j)
        return count


           
       
      


        
     




        