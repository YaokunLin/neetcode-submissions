class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_k = k % len(nums)
        start = len(nums) - new_k
        temp = nums[start:]
        del nums[start:]
        for i in range(new_k):
            nums.insert(i, temp[i])
                
