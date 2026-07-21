class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        l, r = 0, 1
        while r <= len(prices) - 1:
            curr_profit = prices[r] - prices[l]
            if curr_profit >= 0:
                r += 1
            else:
                l = r
                r += 1
            max_val = max(max_val, curr_profit)
        return max_val
        
      


        
        