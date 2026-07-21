from collections import defaultdict
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                left = j - 1
                right = j + 1
                bottom = i + 1
                above = i - 1
                if left >= 0:
                    w = abs(heights[i][j] - heights[i][left])
                    graph[(i, j)].append(((i, left), w))
                if right <= len(heights[0]) - 1:
                    w = abs(heights[i][j] - heights[i][right])
                    graph[(i, j)].append(((i, right), w))
                if bottom <= len(heights) - 1:
                    w = abs(heights[i][j] - heights[bottom][j])
                    graph[(i, j)].append(((bottom, j), w))
                if above >= 0:
                    w = abs(heights[i][j] - heights[above][j])
                    graph[(i, j)].append(((above, j), w))

        min_heap = [(0, (0, 0))]
        dist = {}
        while min_heap:
            cur_height_dif, cur_node = heapq.heappop(min_heap)
            
            if cur_node in dist:
                continue
            dist[cur_node] = cur_height_dif
            for neighbour, weight in graph[cur_node]:
                if neighbour not in dist:
                    heapq.heappush(min_heap, (max(cur_height_dif, weight), neighbour))
        
        return dist[(len(heights) - 1, len(heights[0]) - 1)]
        


        