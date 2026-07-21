class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visit_map = {}
        for num in nums:
            if num not in visit_map:
                visit_map[num] = 1
            else:
                return num 
        

        