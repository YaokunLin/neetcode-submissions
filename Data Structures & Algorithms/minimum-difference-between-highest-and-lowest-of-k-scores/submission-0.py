class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = float("inf")
        for l in range(len(nums) - k + 1):
            r = l + k - 1
            cur_diff = nums[r] - nums[l]
            diff = min(cur_diff, diff)
        return diff