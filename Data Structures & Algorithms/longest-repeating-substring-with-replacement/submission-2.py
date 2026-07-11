from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        highest_freq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            char = s[r]
            counts[char] += 1
            highest_freq = max(highest_freq, counts[char])
            window_len = r - l + 1
            while window_len - highest_freq > k:
                counts[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            res = max(res, window_len)
        return res
        
   
       
      
      
        

            



        