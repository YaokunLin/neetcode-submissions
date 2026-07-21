class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            if num not in nums_map: 
                nums_map[num] = 1
            else:
                nums_map[num] += 1
      
        sorted_vals = sorted(nums_map, key = lambda x: nums_map[x], reverse = True)
    

        
          
        return sorted_vals[:k]


      
       