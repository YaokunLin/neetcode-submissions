class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        else:
            sign = -1
        res = int(str(abs(x))[::-1])
        res = sign * res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        else:
            return res
    

       
          
        

        
        