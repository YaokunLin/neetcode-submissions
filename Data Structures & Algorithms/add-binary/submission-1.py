class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str_sum = int(a, 2) + int(b, 2)
        return str(bin(str_sum))[2:]