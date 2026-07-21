class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_arr = []
            for arr in res:
                new_arr.append(arr + [num])

            res.extend(new_arr)
        final = []
        seen = set()
        for item in res:
            key = tuple(sorted(item))
            if key not in seen:
                seen.add(key)
                final.append(key)
        return final

        