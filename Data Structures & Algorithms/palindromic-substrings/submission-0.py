class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        count = 0
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1
        # handle substrings length is 1 case
        for i in range(n):
            dp[i][i] = True
            count += 1
        # hanle substrings length is 2 case
        for i in range (n - 1):
            if s[i] == s[i+1]:
                dp[i][i + 1] = True
                print(count)
                count += 1
        # handle substrings length is greater than 3 case
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                # end index
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, max_len = i, length
                    count += 1
        return count
            

        