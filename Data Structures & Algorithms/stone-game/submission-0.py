class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l, r = 0, len(piles) - 1
        score_alice = 0
        score_bob = 0
        while l <= r:
            if piles[l] >= piles[r]:
                score_alice += piles[l]
                l += 1
                if piles[l] < piles[r]:
                    score_bob += piles[l]
                    l += 1
                else:
                    score_bob += piles[r]
                    r -= 1
            else:
                score_alice += piles[r]
                r -= 1
                if piles[l] < piles[r]:
                    score_bob += piles[l]
                    l += 1
                else:
                    score_bob += piles[r]
                    r -= 1
        return score_alice > score_bob
            
        