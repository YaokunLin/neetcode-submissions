class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        best = 0
        for num in nums:
            if num == 1:
                count += 1
                best = max(best, count)
            else:
                count = 0
        return best
      
    
            

        