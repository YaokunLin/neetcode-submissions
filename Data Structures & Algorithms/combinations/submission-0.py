class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for num in range(1, n + 1):
            new_arr = []
            for arr in res:
                new_arr.append(arr + [num])
            res.extend(new_arr)
        
        k_arr = []
        
        for arr in res:
            if len(arr) == k:
                k_arr.append(arr)
        return k_arr


        