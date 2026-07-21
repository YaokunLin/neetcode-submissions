class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {i: [] for i in range(n)}
        for node1, node2 in edges:
            map[node1].append(node2)
            map[node2].append(node1)
        visited = set()
        count = 0

        def dfs(node, parent):
            stack = [(node, parent)]

            while stack:
                cur_node, cur_parent = stack.pop()
                visited.add(cur_node)
                for neighbour in map[cur_node]:
                    if neighbour in visited and cur_parent != neighbour:
                        return False
                    elif neighbour not in visited:
                        visited.add(neighbour)
                        stack.append((neighbour, cur_node))
            return True

        for node in map:
            if node not in visited:
                count += 1
                if not dfs(node, -1):
                    return False

        
        if count == 1:
            return True
        else:
            return False




        