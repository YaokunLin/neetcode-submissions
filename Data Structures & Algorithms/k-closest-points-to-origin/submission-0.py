from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        dist_map = {}
        for i in range(len(points)):
            dist = sqrt((points[i][0])**2 + (points[i][1])**2)
            dist_map[i] = dist
      
        sorted_dist = sorted(dist_map.items(), key=lambda x:x[1])
        for j in range(k):
            index = sorted_dist[j][0]
            res.append(points[index])
        return res

        