class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                length = 1
                while nums[i] + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
  


    

  
        
                
    


         
            
        