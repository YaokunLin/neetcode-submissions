class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        cache = {}
        def helper(i, profit, weight, capacity):
            if i == len(profit):
                return 0
            
            if (i, capacity) in cache:
                return cache[(i, capacity)]
            
            # not to include i
            max_profit_not_include_i = helper(i + 1, profit, weight, capacity)

            # to include i
            if capacity < weight[i]:
                cache[(i, capacity)] = max_profit_not_include_i
                return max_profit_not_include_i

            max_profit_include_i = profit[i] + helper(i + 1, profit, weight, capacity - weight[i])
            max_profit = max(
                max_profit_not_include_i, 
                max_profit_include_i
                )
            cache[(i, capacity)] = max_profit
            return max_profit
        
        return helper(0, profit, weight, capacity)
