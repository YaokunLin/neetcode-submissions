class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = [0] * len(nums)
        sub_sum[0] = nums[0]
        for i in range(1, len(nums)):
            if sub_sum[i - 1] > 0:
                sub_sum[i] = sub_sum[i - 1] + nums[i]
            else:
                sub_sum[i] = nums[i]
        return max(sub_sum)

        
        
        