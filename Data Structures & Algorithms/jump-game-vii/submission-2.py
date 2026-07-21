class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        dp = [False] * (len(s))
        dp[0] = True
        count = 0

        for i in range(1, len(s)):
            if s[i] == "1":
                continue
            for j in range(max(i - maxJump, 0), i - minJump + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[len(s) - 1]
     
            

     
            
        