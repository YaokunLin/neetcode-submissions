import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = {i: float("inf") for i in range(1, n + 1)}
        print(dist)
        dist[k] = 0
        for _ in range(n - 1):
            for u, v, t in times:
                if dist[u] != float("inf") and dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t
        for u, v, t in times:
            if dist[u] != float("inf") and dist[u] + t < dist[v]:
                return "negative cycle"
        print(dist)
        max_dist = max(dist.values())
        if max_dist < float("inf"):
            return max_dist
        else:
            return -1

       
      
         

            


        