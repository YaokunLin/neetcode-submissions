class Solution:
    def climbStairs(self, n: int) -> int:
        
       
        memo = {}
        def helper(remain_steps):
            if remain_steps == 0:
                return 1
            if remain_steps < 0:
                return 0

            if remain_steps in memo:
                return memo[remain_steps]
            
            n_ways =  (
                helper(remain_steps - 1) + 
                helper(remain_steps - 2)
                )
            
            memo[remain_steps] = n_ways
            return n_ways
        return helper(n)
    
     

     
        

    
    