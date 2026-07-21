class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_arr = []
            for nums_arr in res:
                new_arr.append(nums_arr + [num])
            res.extend(new_arr)
        return res

     
    


        