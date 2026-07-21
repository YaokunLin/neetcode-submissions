class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current, openCount, closeCount):
            if len(current) == 2*n:
                res.append(current)
                return
            if openCount < n:
                backtrack(current + '(', openCount + 1, closeCount)
            if openCount > closeCount:
                backtrack(current + ')', openCount, closeCount + 1)
        backtrack("", 0, 0)
        return res


    
        