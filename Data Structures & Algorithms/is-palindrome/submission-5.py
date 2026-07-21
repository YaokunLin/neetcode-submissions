class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        l , r = 0, len(res) - 1
        print(res)
        while l < r:
            print(r)
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
     
       

     