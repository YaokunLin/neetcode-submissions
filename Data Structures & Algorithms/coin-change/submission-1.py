class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1): 
            for coin_val in coins:
                remain = i - coin_val
                if remain >= 0:
                    dp[i] = min(dp[i], dp[remain] + 1)
                
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
       


        