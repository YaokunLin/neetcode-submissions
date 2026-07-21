import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        cur = 0
        sorted_trips = sorted(trips, key=lambda x: x[1])
        for passengers, start, end in sorted_trips:
            while heap and heap[0][0] <= start:
                des, p = heapq.heappop(heap)
                cur -= p
            cur += passengers
            if cur > capacity:
                return False
            heapq.heappush(heap, (end, passengers))
        return True




        