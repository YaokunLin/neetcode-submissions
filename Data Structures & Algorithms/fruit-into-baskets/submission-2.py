from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0
        active_fruits = []
        for r in range(len(fruits)):
            counts[fruits[r]]  += 1
        
            while len(counts.keys()) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
               
                l += 1
            window_len = (r - l) + 1
            res = max(res, window_len)
        return res

        