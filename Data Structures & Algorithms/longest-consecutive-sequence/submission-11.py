class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
   
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(list(set(nums)))
        n = len(sorted_nums)
        if n == 1:
            return 1
        count = 0
        length = 1
        for i in range(n - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
              
                length += 1
            else:
                length = 1
        
            count = max(count, length )
        return count

        
                
    


         
            
        