class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        sorted_map = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))
        first_key = next(iter(sorted_map))
      
        return first_key
        