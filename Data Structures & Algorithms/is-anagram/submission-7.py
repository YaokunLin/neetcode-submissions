from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getStringDict(st):
            s_map = defaultdict(int)
            for char in st:
                s_map[char] += 1
            return s_map
        return getStringDict(s) == getStringDict(t)


        
    
        
        
       
        