class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        l = 0
        r = len(filtered_s) - 1
        print(filtered_s)
        while l < len(filtered_s) and r >= 0:
            if filtered_s[l] == filtered_s[r]:
                l += 1
                r -= 1
            else:
                print(filtered_s[l])
                print(filtered_s[r])
                return False
              
        return True
        