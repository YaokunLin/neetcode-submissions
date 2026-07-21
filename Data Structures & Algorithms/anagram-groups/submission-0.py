from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for i in str:
                count[ord(i) - ord('a')] += 1
            ans[tuple(count)].append(str)
        return ans.values()
       
        