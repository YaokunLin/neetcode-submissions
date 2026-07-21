class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1
        for char_t in t:
            if char_t not in t_map:
                t_map[char_t] = 1
            else:
                t_map[char_t] += 1
        return s_map == t_map
        
        