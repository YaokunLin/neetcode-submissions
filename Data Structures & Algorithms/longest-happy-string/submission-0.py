import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = []
        maxheap = []

        for count, ch in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if count != 0:
                heapq.heappush(maxheap, (count, ch))

        while maxheap:
            count1, ch1 = heapq.heappop(maxheap)
            if len(res) >= 2 and res[-1] == ch1 and res[-2] == ch1:
                if not maxheap:
                    break
                count2, ch2 = heapq.heappop(maxheap)
                count2 += 1
                res.append(ch2)
                if count2 < 0:
                    heapq.heappush(maxheap, (count2, ch2))
                heapq.heappush(maxheap, (count1, ch1))
            else:
                res.append(ch1)
                count1 += 1
                if count1 < 0:
                    heapq.heappush(maxheap, (count1, ch1))
        return "".join(res)
            
        