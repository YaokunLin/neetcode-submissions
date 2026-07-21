class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        parent = [i for i in range(len(points))]
        rank = [1] * len(points)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                edges.append((weight, i, j))
        
        def find(i):
            if parent[i] != i:
                return find(parent[i])
            else:
                return parent[i]

        def union(u, v):

            parent_u = find(u)
            parent_v = find(v)

            if parent_u != parent_v:
                if rank[parent_u] > rank[parent_v]:
                    parent[parent_v] = parent_u
                elif rank[parent_u] < rank[parent_v]:
                    parent[parent_u] = parent_v
                else:
                    parent[parent_u] = parent_v
                    rank[parent_v] += 1

        res = 0
        count = 0
        edges.sort()
        for weight, source, des in edges:
            rep_i = find(source)
            rep_j = find(des)
            if rep_i != rep_j:
                res += weight
                count += 1
                union(source, des)
                if count == len(points) - 1:
                    break

        return res

            


            


        

        
    


        