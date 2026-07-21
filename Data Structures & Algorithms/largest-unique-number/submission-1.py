class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        sorted_map = dict(sorted(map.items(), reverse=True))
       
        for val, freq in sorted_map.items():
            if freq == 1:
                return val
        return -1

 
        