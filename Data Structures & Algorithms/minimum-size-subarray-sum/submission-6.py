class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if total < target:
            return 0
        res = float("inf")
        for i in range(len(nums)):
            l = i
            r = i
            cur_sum = nums[r]
            while r < len(nums):
                if cur_sum < target:
                    r += 1
                    if r < len(nums):
                        cur_sum += nums[r]
                else:
                    res = min(res, r - l + 1)
                    break
        return res
            


                
      
       

          
        





            

                

            


            
        