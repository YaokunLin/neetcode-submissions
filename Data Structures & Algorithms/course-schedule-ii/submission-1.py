class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {}
        for i in range(numCourses):
            map[i] = []
        for course, pre in prerequisites:
            map[pre].append(course)
        visited = set()
        cycle = set()
        res = []
        print(map)

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for neighbour in map[c]:
                if dfs(neighbour) == False:
                    return False
            
            cycle.remove(c)
            visited.add(c)
            
            res.append(c)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res[::-1]