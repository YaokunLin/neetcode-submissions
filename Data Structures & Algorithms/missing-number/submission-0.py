class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        for num in range(len(nums) + 1):
            res = res ^ num
        return res

        