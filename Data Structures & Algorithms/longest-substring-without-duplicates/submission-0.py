class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charmap = {}
        max_len = 0
        for r, char in enumerate(s):
            if char in charmap and charmap[char] >= l:
                l = charmap[char] + 1
            charmap[char] = r
            max_len = max(max_len, r - l + 1)
        return max_len

       


        