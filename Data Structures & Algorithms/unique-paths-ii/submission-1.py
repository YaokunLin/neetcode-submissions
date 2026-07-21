class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        # left column
        for row in range(len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                break
            else:
                dp[row][0] = 1
        # top row
        for col in range(len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                break
            else:
                dp[0][col] = 1
        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                if obstacleGrid[r - 1][c] == 1 and obstacleGrid[r][c - 1] == 1:
                    dp[r][c] = 0
                elif obstacleGrid[r - 1][c] == 1 and obstacleGrid[r][c - 1] == 0:
                    dp[r][c] = dp[r][c - 1]
                elif obstacleGrid[r - 1][c] == 0 and obstacleGrid[r][c - 1] == 1:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
