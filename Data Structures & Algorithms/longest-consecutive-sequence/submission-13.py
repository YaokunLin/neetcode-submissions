class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        count = 1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                count += 1
                res[i] = count
            elif nums[i] == nums[i - 1]:
                res[i] = count
            else:
                count = 1
        return max(res)

  
        
                
    


         
            
        