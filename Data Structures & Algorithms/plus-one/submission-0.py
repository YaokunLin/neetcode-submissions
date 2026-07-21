class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
          
            num += digits[i] * 10**(len(digits) - 1 - i)
        print(num)
        new_num = num + 1
        new_num_str = str(new_num)
        res = []
        for d in new_num_str:
            res.append(int(d))
        return res




        