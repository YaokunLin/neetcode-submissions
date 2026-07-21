class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitsSum(n):
            total = 0
            while n > 0:
                a = n % 10
                total += a**2
                n = n // 10
            return total
        seen = set()
        digits_sum = n

        while digits_sum != 1:
            if digits_sum in seen:
                return False
            seen.add(digits_sum)
            digits_sum = getDigitsSum(digits_sum)
        return True



      
        
            



        