class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            preMap[course].append(pre)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for preCrs in preMap[crs]:
                if not dfs(preCrs):
                    return False
            preMap[crs] = []
            visit.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        