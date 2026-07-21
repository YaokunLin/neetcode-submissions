class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def rob(i):
            if i == len(nums) - 1:
                return nums[-1]
            if i > len(nums) - 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            max_profit = max(
                nums[i] + rob(i + 2),
                rob(i + 1)
            )
            memo[i] = max_profit

            return max_profit
        
        return rob(0)

   
    
            
            
        