class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        count = 0
        res = 0
        need_rep = 0
        for r in range(len(nums)):
            # need replacement
            if nums[r] == 1:
                count += 1
            cur_window = r - l + 1
            need_rep = cur_window - count
            while need_rep > 1:
                if l < len(nums) and nums[l] == 1:
                    count -= 1
                l += 1
                need_rep = r - l + 1 - count
            res = max(res, r - l + 1)
        return res
            

        


        