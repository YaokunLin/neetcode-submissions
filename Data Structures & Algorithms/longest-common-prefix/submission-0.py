class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
    
        for i in range(len(prefix)):
            for j in range(1, len(strs)):
                if len(strs[j]) == len(prefix[:i]) or strs[j][i] != prefix[i]:
                    return prefix[:i]
        return prefix
  