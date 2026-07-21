class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        M = (L + R) // 2

        while L <= R:
            if nums[M] == target: 
                return M
            if nums[M] < target:
                L = M + 1
            else:
                R = M - 1
            M = (L + R) // 2
        return -1
        
        

        
      
        