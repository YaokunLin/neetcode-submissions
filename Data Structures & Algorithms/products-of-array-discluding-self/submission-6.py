class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_prefix = {0: 1}
        nums_suffix = {len(nums) - 1: 1}
        for i in range(1, len(nums)):
            nums_prefix[i] = nums_prefix[i - 1] * nums[i - 1]
     
        for j in range(len(nums) - 2, -1, -1):
            nums_suffix[j] = nums_suffix[j + 1] *nums[j + 1]
     
        res = []

        for index in range(len(nums)):
            res.append(nums_prefix[index] * nums_suffix[index])
        return res



        

   

        






            
       
      

        