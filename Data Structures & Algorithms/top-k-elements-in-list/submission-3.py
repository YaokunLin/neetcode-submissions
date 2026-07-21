from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1

        sorted_nums_count = sorted(nums_count.items(), key=lambda item:item[1], reverse=True)[:k]
        res = []
        for num, count in sorted_nums_count:
            res.append(num)
        return res

       


      
       