from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for chr in s:
            s_counter[chr] += 1
        
        for chr in t:
            t_counter[chr] += 1
        
        return s_counter == t_counter

        
    
        
        
       
        