class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_data = set()
        for num in nums:
            if num not in set_data:
                set_data.add(num)
            else:
                return True
        return False
        
     
            
        

    