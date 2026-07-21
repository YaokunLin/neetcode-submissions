from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(heap)
        prev_freq, prev_char = 0, ""

        res = []

        while heap:
            freq, char = heapq.heappop(heap)
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            res.append(char)
            freq += 1
            prev_freq = freq
            prev_char = char
        
        if len(res) == len(s):
            return "".join(res)
        else:
            return ""

            
            
            
