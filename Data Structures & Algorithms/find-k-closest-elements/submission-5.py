class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_map = {}
        for i in range(len(arr)):
            closest_map[i] = abs(arr[i] - x)
        sorted_map = sorted(closest_map.items(), key = lambda item: (item[1], item[0]))
        res = []
        for key, val in sorted_map[:k]:
            res.append(arr[key])
        res.sort()
        return res

      
    
       

        