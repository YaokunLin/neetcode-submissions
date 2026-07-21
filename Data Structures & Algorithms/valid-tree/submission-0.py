class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {i: [] for i in range(n)}
        for node1, node2 in edges:
            map[node1].append(node2)
            map[node2].append(node1)
        visited = set()
        count = 0

        def dfs(node, parent):
            visited.add(node)
            for neighbour in map[node]:
                if neighbour not in visited:
                    if not dfs(neighbour, node):
                        return False
                elif neighbour != parent:
                    return False
            return True

        for node in map:
            if node not in visited:
                count += 1
                if not dfs(node, -1):
                    print('ddd')
                    return False

        
        if count == 1:
            return True
        else:
            return False




        