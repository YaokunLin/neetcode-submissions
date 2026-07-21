class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m + 1)]
     
        #first column
        for r in range(m):
            dp[r][0] = 1
        #top row
        for c in range(n):
            dp[0][c] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                print('i', i)
                print('j', j)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
        