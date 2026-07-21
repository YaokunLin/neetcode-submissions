class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(arr):
            if len(arr) == 0:
                res.append(path.copy())
                return
            
            for i in range(len(arr)):
                num = arr[i]
                path.append(num)
                cur_arr = arr[:i] + arr[i+1:]
                dfs(cur_arr)
                path.pop()
        dfs(nums)
        
        return res