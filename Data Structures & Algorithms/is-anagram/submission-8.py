from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        s_n, t_n = len(sorted_s), len(sorted_t)
        if s_n != t_n:
            return False
        i = 0
        while i < s_n:
            if sorted_s[i] != sorted_t[i]:
                return False
            else:
                i += 1
        return True
      


        
    
        
        
       
        