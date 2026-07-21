class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node, parent):
            height = 0
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                height = max(height, 1 + dfs(neighbour, node))
            return height
        min_height = n
        res = []
        for i in range(n):
            cur_height = dfs(i, -1)
            if cur_height < min_height:
                res = [i]
                min_height = cur_height
            elif cur_height == min_height:
                res.append(i)
        return res
       



        