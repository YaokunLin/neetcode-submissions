class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph  = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        
        def dfs(node, visited):
            height = 0 
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                   height = max(height, 1 + dfs(neighbour, visited))
            return height

        res = []
        min_height = n
        for i in range(n):
            visited = set()
            visited.add(i)
            cur_height = dfs(i, visited)
            if cur_height < min_height:
                res = [i]
                min_height = cur_height
            elif cur_height == min_height:
                res.append(i)
            
        return res



        