class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(num)
                dfs(i + 1, remain - num)
                path.pop()
            
        dfs(0, target)
        return res

        