class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        F = {}
        F[0] = 0
        F[1] = 0
        for i in range(2, n + 1):
            if F[i - 1] + cost[i - 1] >= F[i - 2] + cost[i -2]:
                F[i] = F[i - 2] + cost[i -2]
            else:
                F[i] = F[i - 1] + cost[i - 1]
        return F[n]


            
    
    
       