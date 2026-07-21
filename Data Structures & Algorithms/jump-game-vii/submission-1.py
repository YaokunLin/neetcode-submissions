class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        dp = [False] * (len(s))
        dp[0] = True
        count = 0

        for i in range(1, len(s)):
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1
            if s[i] == "0" and count > 0:
                dp[i] = True
        return dp[len(s) - 1]
            

     
            
        