class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start):
            n = len(nums)
            res.append(path.copy())
            for i in range(start, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
     
     
    


        