class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False

        window_s1 = [0] * 26
        window_s2 = [0] * 26
        for i in range(len_s1):
            ord_s1 = ord(s1[i]) - ord("a")
            window_s1[ord_s1] += 1
            ord_s2 = ord(s2[i]) - ord("a")
            window_s2[ord_s2] += 1

        if window_s1 == window_s2:
            return True
        for r in range(len_s1, len_s2):
            new_ord = ord(s2[r]) - ord("a")
            window_s2[new_ord] += 1

            old_left = r - len(s1)
            old_left_ord = ord(s2[old_left]) - ord("a")
            window_s2[old_left_ord] -= 1
            
            if window_s2 == window_s1:
                return True
        return False


            


  
        
  
      


    

