class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        #initialize 
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        #first slicing window
        for i in range(len_s1):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        # loop through follown window
        for i in range(len_s2 - len_s1):
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[i]) - ord('a')] -= 1
            count_s2[ord(s2[i + len_s1]) - ord('a')] += 1
            print(count_s1)
            print(count_s2)
        # check the last windown

        return count_s1 == count_s2

      


    

