class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
          
            if num_map[num] > len(nums) // 2:
                return num
    