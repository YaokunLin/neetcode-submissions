class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for num in nums:
            for t in range(1, target + 1):
                if t >= num:
                    for arr in dp[t - num]:
                        dp[t].append(arr + [num])
        return dp[target]