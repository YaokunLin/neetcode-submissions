class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        n = len(s)
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return
            for start in range(i, n):
                sub = s[i : start + 1]
                if ispalindrome(sub):
                    path.append(sub)
                    dfs(start + 1)
                    path.pop()
        def ispalindrome(substrings):
            s_len = len(substrings)
            l, r = 0, s_len - 1
            while l <= r:
                if substrings[l] != substrings[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        dfs(0)
        return res


        