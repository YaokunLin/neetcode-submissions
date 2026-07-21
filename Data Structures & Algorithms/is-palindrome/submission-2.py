class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = []
        for char in s:
            if char.isalnum():
                alph.append(char.lower())
        clean_str = "".join(alph)
        l = 0
        n = len(clean_str)
        r = n - 1
        while l < r:
            if clean_str[l] == clean_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

       

     