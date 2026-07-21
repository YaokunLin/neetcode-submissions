class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        def dfs(i, res_subsets):
            if i == len(nums):
                return res_subsets
            return dfs(i + 1, [[nums[i]] + subset for subset in res_subsets]) + dfs(i + 1,  res_subsets)
        
        return dfs(0, [[]])

        
     
     
    


        