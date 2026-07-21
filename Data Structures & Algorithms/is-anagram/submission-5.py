class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for s_char in s:
            if s_char not in s_map:
                s_map[s_char] = 1
            else:
                s_map[s_char] += 1
            
        t_map = {}
        for t_char in t:
            if t_char not in t_map:
                t_map[t_char] = 1
            else:
                t_map[t_char] += 1
        return t_map == s_map
    
        
        
       
        