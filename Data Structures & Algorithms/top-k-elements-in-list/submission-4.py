from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        sorted_items = sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)
        top_k = sorted_items[:k]
        res = []
        for key, value in top_k:
            res.append(key)
        return res

 

       


      
       