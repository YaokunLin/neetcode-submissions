from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            str_dict = defaultdict(int)
            for char in str:
                str_dict[char] += 1
            key = tuple(sorted(str_dict.items()))
            groups[key].append(str)
        return list(groups.values())
       
                    





     
        