class Solution:
    def rob(self, nums: List[int]) -> int:
        F = [0] * len(nums)
        #hanle the case n = 1
        if len(nums) == 1:
            return nums[0]
        F[0] = nums[0]
        F[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def helper(sub_nums):
            F = [0] * len(sub_nums)
            F[0] = sub_nums[0]
            F[1] = max(sub_nums[0], sub_nums[1])
            for i in range(2, len(sub_nums)):
                F[i] = max(F[i - 2] + sub_nums[i], F[i - 1])
            return F[-1]
    
        max_F = helper(nums[:-1])
        max_S = helper(nums[1:])
        print(max_S)
        print(max_F)
        return max(max_F, max_S)


        