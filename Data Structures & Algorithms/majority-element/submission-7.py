from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        return max(nums_dict, key=nums_dict.get)



