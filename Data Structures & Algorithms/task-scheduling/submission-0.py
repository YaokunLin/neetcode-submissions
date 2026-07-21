import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_map = {}
        for t in tasks:
            if t not in t_map:
                t_map[t] = 1
            else:
                t_map[t] += 1
        
        heap = [(-count, key) for key, count in t_map.items()]
        heapq.heapify(heap)
        time = 0

        while heap:
            temp = []
            for i in range(n + 1):
                if heap:
                    cur_count, cur_key = heapq.heappop(heap)
                    cur_count += 1
                    if cur_count < 0:
                        temp.append((cur_count, cur_key))
                time += 1
                if not heap and not temp:
                    return time
            if len(temp) > 0:
                for cur_count, cur_key in temp:
                    heapq.heappush(heap, (cur_count, cur_key))

        return time

                    

        

       
     
                
