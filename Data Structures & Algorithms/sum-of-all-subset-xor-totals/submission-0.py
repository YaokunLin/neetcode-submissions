class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, sum):
            if i == len(nums):
                return sum
            
            return dfs(i + 1, sum ^ nums[i]) + dfs(i + 1, sum)
        
        return dfs(0, 0)
        