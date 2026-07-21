class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      
        while len(stones) > 1:
            sorted_stones = sorted(stones, reverse=True)
            largest = sorted_stones[0]
            sec_large = sorted_stones[1]
            if largest == sec_large:
                sorted_stones.remove(largest)
                sorted_stones.remove(sec_large)
               
            else:
                sorted_stones.remove(largest)
                sorted_stones.remove(sec_large)
                sorted_stones.append(largest - sec_large)
            stones = sorted_stones
        if not stones:
            return 0
        else:
            return stones[0]
                

                
        