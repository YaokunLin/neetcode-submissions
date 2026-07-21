from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1
        
        res = []
        for key, value in nums_map.items():
            if value > len(nums) / 3:
                res.append(key)
        return res

            

        