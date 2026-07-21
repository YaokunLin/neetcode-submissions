class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_set = set()
        for num in nums:
            if num not in new_set:
                new_set.add(num)
            else:
                return num
        
      
        

        