class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            num = nums[i]
            left = target - nums[i]
            if left not in nums_map:
                nums_map[num] = i
            else:
                return [nums_map[left], i]
      
  


        

        