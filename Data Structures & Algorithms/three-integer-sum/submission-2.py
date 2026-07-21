class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        res = []
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            while l < r:
                total_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if total_sum == 0:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
                    # while sorted_nums[r] == sorted_nums[r + 1] and l < r:
                    #     r -= 1
                if total_sum < 0:
                    l += 1
                if total_sum > 0:
                    r -= 1
        return res
                
            
            
     
            
        
                
   
        
        