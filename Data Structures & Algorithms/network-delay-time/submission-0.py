import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        # initial starting point is k node and at time 0
        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)
            if cur_node in dist:
                continue
            dist[cur_node] = cur_time
            for neighbour, weight in graph[cur_node]:
                if neighbour not in dist:
                    heapq.heappush(min_heap, (weight + cur_time, neighbour))
        
        if len(dist) <= n - 1:
            return -1
        return max(dist.values())
         

            


        