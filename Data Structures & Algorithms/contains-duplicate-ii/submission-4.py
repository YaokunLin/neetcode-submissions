from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = defaultdict(list)
        for i, num in enumerate(nums):
            nums_map[num].append(i)
        
        for index_list in nums_map.values():
            for i in range(1, len(index_list)):
                if index_list[i] - index_list[i - 1] <= k:
                    return True
      
        return False




      

        