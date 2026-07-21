class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = True if (r - l) % 2 else False
            if even:
                left = piles[l]
            else:
                left = 0
            if even:
                right = piles[r]
            else:
                right = 0
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return dp[(l, r)]
        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score
      
            
        