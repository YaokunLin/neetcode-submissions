class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        max_prof = 0
        L, R = 0, 1

        while R <= len(prices) - 1:
            if prices[R] > prices[L]:
                cur_prof = prices[R] - prices[L]
                max_prof = max(max_prof, cur_prof)
            else:
                # found a lower price, reset the buy pointer
                L = R
            R += 1
        return max_prof


        
        
      


        
        