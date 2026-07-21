class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #LIS[i]: the length of the longest increasing subsequence ending at index i
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)
      
    
            
        
        