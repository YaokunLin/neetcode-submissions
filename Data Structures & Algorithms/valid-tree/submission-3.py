class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {i: [] for i in range(n)}
        for a, b in edges:
            map[a].append(b)
            map[b].append(a)
        visited =  set()
        count = 0

        def explore(node, parent):
            stack = [(node, parent)]
            while stack:
                cur_node, cur_parent = stack.pop()
                visited.add(cur_node)
                for neighbour in map[cur_node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append((neighbour, cur_node))
                    elif neighbour != cur_parent:
                        return False
            return True
        
        for i in range(n):
            if i not in visited:
                count += 1
                if not explore(i, -1):
                    return False
        
        if count == 1:
            return True
        else:
            return False


      

     
  




        