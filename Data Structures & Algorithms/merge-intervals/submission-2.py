import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda interval: interval[0])

        prev_end = 0
        res = []
      
      
        for interval in intervals:
            if res and interval[0] <= prev_end:
                res[-1][1] = max(prev_end, interval[1])
                prev_end = max(prev_end, interval[1])
            else:
                res.append([interval[0], interval[1]])
                prev_end = interval[1]
     
        return res



        