class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            cur_profit = prices[r] - prices[l]
            if cur_profit >= 0:
                max_profit = max(cur_profit, max_profit)
                r += 1
            else:
                l = r
                r = l + 1
        return max_profit



        
        
      


        
        