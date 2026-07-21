class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        for i, c in enumerate(s):
            hash_map[c] = i
        
        res = []
        end = 0
        size = 0
        
        for i, c in enumerate(s):
            end = max(end, hash_map[c])
            size += 1
            if i == end:
              
                res.append(size)
                size = 0
        return res


        