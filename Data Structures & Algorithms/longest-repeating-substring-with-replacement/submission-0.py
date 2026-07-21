class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0
      
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_val = max(count.values())
            remaining = r - l + 1 - max_val
            if remaining <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        return res
        

            



        