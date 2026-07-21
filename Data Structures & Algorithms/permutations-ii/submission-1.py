class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)
        
        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
             

                num = nums[i]
                path.append(num)
                used[i] = True
                dfs()
                used[i] = False
                path.pop()
        dfs()
        return res
                