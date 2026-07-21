class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)

        def is_divisor(l):
            if str1_len % l != 0 or str2_len % l != 0:
                return False
            f1, f2 = str1_len // l, str2_len // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
            


        for l in range(min(str1_len, str2_len), 0, -1):
            if is_divisor(l):
                return str1[:l]
        return ""

        