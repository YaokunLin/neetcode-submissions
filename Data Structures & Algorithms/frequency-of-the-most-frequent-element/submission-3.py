class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        operation = 0
        res = 1
        for r in range(1, len(nums)):
            operation += (nums[r] - nums[r - 1]) * (r - l)
            while operation > k:
                diff = nums[r] - nums[l]
                l += 1
                operation -= diff
       
            window_len = r - l + 1
            res = max(window_len, res)
        return res
