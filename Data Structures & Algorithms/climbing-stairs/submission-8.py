class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        n_ways = [0] * (n + 1)
        n_ways[1] = 1
        n_ways[2] = 2

        for n_steps in range(3, n + 1):
            n_ways[n_steps] = n_ways[n_steps - 1] + n_ways[n_steps - 2]
        
        return n_ways[n]


    
     

     
        

    
    