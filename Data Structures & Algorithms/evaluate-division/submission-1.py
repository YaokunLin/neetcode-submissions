from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        def dfs(s, t, visited):
            if s not in graph or t not in graph:
                return -1
            if s == t:
                return 1
            visited.add(s)
            for nei, w in graph[s]:
                if nei not in visited:
                    result = dfs(nei, t, visited)
                    if result != -1:
                        return w * result
            return -1

        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res                     
               
               
               
               

               
               
               
                
        
        

        