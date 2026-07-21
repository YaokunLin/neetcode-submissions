class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            small_val = amount + 1
           
            for coin_val in coins:
                remain = i - coin_val
                if remain >= 0 and 1 + dp[remain] <= small_val:
                   
                    small_val = 1 + dp[remain]
                dp[i] = small_val
                
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
       


        