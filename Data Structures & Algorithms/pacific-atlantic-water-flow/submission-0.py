class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(row,  col, visited):
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] < heights[row][col]:
                    continue
                dfs(nr, nc, visited)
                
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        return list([r, c] for r, c in pacific & atlantic)
        
      
            
        