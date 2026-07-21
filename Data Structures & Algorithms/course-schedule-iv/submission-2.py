class Solution:
        def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
            graph = {i: [] for i in range(numCourses)}
            for a, b in prerequisites: 
                graph[a].append(b)
            def dfs(node1, node2, visited):
                if node1 in visited:
                    return False
                visited.add(node1)
                for neighbour in graph[node1]:
                    if neighbour == node2:
                        return True
                    elif dfs(neighbour, node2, visited):
                        return True
                return False
            res = []
            for node1, node2 in queries:
                visited = set()
                if dfs(node1, node2, visited):
                    res.append(True)
                else:
                    res.append(False)
            return res

            

                    