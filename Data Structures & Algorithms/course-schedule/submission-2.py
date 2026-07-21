class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            map[prereq].append(course)
        visited = set()
        def dfs(c):
            if c in visited:
                return False
            visited.add(c)
            for neighbour in map[c]:
                if not dfs(neighbour):
                    return False
            visited.remove(c)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            




        