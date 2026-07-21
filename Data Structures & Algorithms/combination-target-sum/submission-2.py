class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        path = []
        res = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
           
            for i in range(start, len(nums)):
                if nums[start] > remain:
                    break
                num = nums[i]
                path.append(num)
                dfs(i, remain - num)
                path.pop()
        
        dfs(0, target)

        return res