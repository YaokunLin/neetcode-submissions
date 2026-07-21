class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0] = 0
        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp[1] = nums[0]

        for i in range(2, n + 1):
            print(i)
            if dp[i - 1] < dp[i - 2] + nums[i - 1]:
                dp[i] = dp[i - 2] + nums[i - 1]
            else:
                dp[i] = dp[i - 1]
        
        return dp[n]

   
    
            
            
        