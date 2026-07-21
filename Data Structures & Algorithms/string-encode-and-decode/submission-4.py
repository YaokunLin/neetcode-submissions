class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str_val in strs:
            res += str(len(str_val)) +  "#" + str_val
        return res
      

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            temp = s[start:end]
            res.append(temp)
            i = end
        return res

 
                




   
