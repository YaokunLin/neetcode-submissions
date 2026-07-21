class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigit(n):
            res = []
            while n > 0:
                a = n % 10
                res.append(a)
                n = n // 10
            return res

        digits_sum = n
        seen = set()
        while digits_sum != 1:
            if digits_sum in seen:
                return False
            seen.add(digits_sum)

            n_digits = getDigit(digits_sum)
            new_sum = 0
            for digit in n_digits:
                new_sum += digit**2

            digits_sum = new_sum
          
        return True

      
        
            



        