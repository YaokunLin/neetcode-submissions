from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        s_map = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            s_map[key].append(s)
        return list(s_map.values())

                    
      
       
                    





     
        