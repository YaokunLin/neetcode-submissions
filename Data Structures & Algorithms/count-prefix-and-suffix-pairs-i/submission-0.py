class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        if len(str1) > len(str2):
            return False
        for i, chr1 in enumerate(str1):
            # check prefix
            chr2 = str2[i]
            if chr1 != chr2:
                return False
            
            # check suffix
            j = len(str1) - i
            chr2 = str2[-j] # this goes from the back
            if chr1 != chr2:
                return False
        return True
            
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if len(words) <= 1:
            return 0
        
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words), 1):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res

        