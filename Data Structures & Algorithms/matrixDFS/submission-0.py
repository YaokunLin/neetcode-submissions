class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        # Edge case: If the start is blocked
        if grid[0][0] == 1:
            return 0

        # Stack holds tuples of: (Action, row, col)
        stack = [("ENTER", 0, 0)]
        visit = set()
        count = 0

        # Down, Up, Right, Left (Matches your recursive sequence)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            action, r, c = stack.pop()

            # If we hit an EXIT marker, it means we finished exploring 
            # all children of this cell. Time to backtrack!
            if action == "EXIT":
                visit.remove((r, c))
                continue

            # Standard boundary and validity checks
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                grid[r][c] == 1 or (r, c) in visit):
                continue

            # If we reached the destination
            if r == ROWS - 1 and c == COLS - 1:
                count += 1
                continue

            # Mark the current cell as visited
            visit.add((r, c))

            # LIFO Stack Order: We must push the EXIT action FIRST so that 
            # it is popped LAST (after all children are explored).
            stack.append(("EXIT", r, c))

            # Push all 4 directions to the stack
            for dr, dc in directions:
                stack.append(("ENTER", r + dr, c + dc))

        return count