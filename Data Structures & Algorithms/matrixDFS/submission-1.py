class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        if grid[0][0] == 1:
            return 0

        # Stack holds tuples of: (row, col, set_of_visited_cells)
        # We initialize it with the starting coordinate already in the set.
        stack = [(0, 0, {(0, 0)})]
        count = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            r, c, visited = stack.pop()

            # If we reached the destination
            if r == ROWS - 1 and c == COLS - 1:
                count += 1
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and valid cells
                if (0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    grid[nr][nc] == 0 and 
                    (nr, nc) not in visited):
                    
                    # Create a new copy of the visited set for this specific branch
                    new_visited = visited.copy()
                    new_visited.add((nr, nc))
                    
                    stack.append((nr, nc, new_visited))

        return count