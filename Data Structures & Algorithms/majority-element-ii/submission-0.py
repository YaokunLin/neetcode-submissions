class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
         
        for val in num_map:
            if num_map[val] > len(nums) // 3:
                res.append(val)

        return res
        