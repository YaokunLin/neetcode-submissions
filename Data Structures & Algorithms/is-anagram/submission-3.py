class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = self.hash_map(s)
        t_map = self.hash_map(t)
        return s_map == t_map
     
        
    def hash_map(self, s: str) -> dict:
        visited_map = {}
        for char in s:
            if char not in visited_map:
                visited_map[char] = 1
            else:
                visited_map[char] += 1
        return visited_map

        