class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      
        while len(stones) > 1:
            sorted_stones = sorted(stones)
            cur = sorted_stones.pop() - sorted_stones.pop()
            if cur > 0:
                sorted_stones.append(cur)
            stones = sorted_stones
       
        if not stones:
            return 0
        else:
            return stones[0]
                

                
        