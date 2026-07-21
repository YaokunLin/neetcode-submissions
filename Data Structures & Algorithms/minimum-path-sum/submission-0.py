class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for i in range(n)]
        dp[0][0] = grid[0][0]
        
        # top row:
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # left column:
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
        return dp[n - 1][m - 1]
        