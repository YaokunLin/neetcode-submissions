import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = []
        for i, task in enumerate(tasks):
            sorted_tasks.append((task[0], task[1], i))
        sorted_tasks.sort()

        heap = []
        time = 0
        res = []
        i = 0

        while i < len(sorted_tasks) or heap:
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1

            process_time, index = heapq.heappop(heap)
            time += process_time
            res.append(index)
        return res




        