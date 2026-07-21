class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_k = k % len(nums)
        l, r = 0, len(nums) - 1
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1
                r -= 1
        reverse(0, len(nums) - 1)
        reverse(0, new_k - 1)
        reverse(new_k, len(nums) - 1)

      
                
