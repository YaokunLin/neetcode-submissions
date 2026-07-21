class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        start, max_len = 0, 1
        dp = [[False] * n for _ in range(n)]
        #handle palindrome length 1 case
        for i  in range(n):
            dp[i][i] = True
        # handle palindrome length 2 case
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                start, max_len = i, 2
        # handle palindrome length more than 3 case
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                # end index
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, max_len = i, length
        return s[start: start + max_len ]

