class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
              
                total = res[i + j] + product
                digit = total % 10
                carry = total // 10
                res[i + j] = digit
                res[i + j + 1] += carry
        lead = 0
        res = res[::-1]
        while lead < len(res) and res[lead] == 0:
           lead += 1
        res = res[lead:]
        return "".join(map(str, res))

       
        