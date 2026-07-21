class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_sets = set()
        for num in nums:
            if num not in num_sets:
                num_sets.add(num)
            else:
                return True
        return False
            
        

    