class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1
            else:
                prefix = prefix * nums[i - 1]

                res[i] = prefix 
        post_fix = 1
        print(res[i])
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * post_fix
            post_fix = post_fix * nums[j]
        return res

        