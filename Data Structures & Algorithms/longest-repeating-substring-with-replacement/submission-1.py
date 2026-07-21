class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        best = 0
        l = 0 
        max_freq = 0
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            max_freq = max(max_freq, count[index])
            
            while r - l + 1 - max_freq > k:
                l_index = ord(s[l]) - ord('A')
                count[l_index] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
       
      
      
        

            



        