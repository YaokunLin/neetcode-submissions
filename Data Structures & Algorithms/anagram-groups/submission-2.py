from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        added = [False] * len(strs)
        for i in range(len(strs)):
            temp = []
            if added[i]:
                continue
            temp.append(strs[i])
            for j in range(i + 1, len(strs)):
                if added[j]:
                    continue
                if sorted(strs[i]) == sorted(strs[j]):
                    temp.append(strs[j])
                    added[i] = True
                    added[j] = True
            res.append(temp)
        return res
                    
      
       
                    





     
        