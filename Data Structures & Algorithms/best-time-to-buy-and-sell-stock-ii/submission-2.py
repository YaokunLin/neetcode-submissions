class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l , r = 0, 1
        res = 0
        while r <= n - 1:
            if prices[r] > prices [l]:
                res += prices[r] - prices[l]
                l += 1
                r += 1
            else:
                l += 1
                r += 1
        return res




  



            

        