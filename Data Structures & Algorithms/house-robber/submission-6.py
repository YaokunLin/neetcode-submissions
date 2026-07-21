class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        F = {}
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        F[0] = nums[0]
        F[1] = max(nums[0], nums[1])
        for i in range (2, n): 
            #F[i] = max(F[i - 1], F[i - 2] + nums[i])
            if F[i - 1] < F[i - 2] + nums[i]:
                F[i] = F[i - 2] + nums[i]
            else:
                F[i] = F[i - 1]
        return F[n - 1]
            
            
        