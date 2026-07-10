class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)
        for i in range(n_s2 - n_s1 + 1):
            l = i
            r = l + n_s1 - 1
            while r < n_s2:
                sorted_s2_sub = sorted(s2[l: r + 1])
                if sorted_s2_sub == sorted(s1):
                    return True
                else:
                    l = r + 1
                    r = l + n_s2 - 1
        return False
        
  
      


    

