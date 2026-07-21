class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = {i: [] for i in range(n)}
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
        visited = set()
        count = 0

        def explore(node):
            visited.add(node)
            for neighbour in map[node]:
                if neighbour not in visited:
                    explore(neighbour)
        


        for node in range(n):
            if node not in visited:
                count += 1
                explore(node)
        return count

        