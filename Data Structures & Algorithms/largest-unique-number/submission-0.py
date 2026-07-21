class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        while nums:
            max_val = max(nums)
            max_val_count = nums.count(max_val)
            print(max_val)
            if max_val_count > 1:
                for _ in range(max_val_count):
                    nums.remove(max_val)
            elif max_val_count == 1:
                return max_val
        return -1

        