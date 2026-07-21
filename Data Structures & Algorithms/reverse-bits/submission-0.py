class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        for i in range(32):
            if n & (1 << i):
                res.append(1)
            else:
                res.append(0)

        val = 0
      
        for i in range(len(res)):
            val += res[i] * 2**(len(res) - 1 - i)
        return val





        