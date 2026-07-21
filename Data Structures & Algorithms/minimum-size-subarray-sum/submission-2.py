class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = set()
        i = 0
        def calculate_sum(arr):
            sum_val = 0
            for num in arr:
                sum_val += num
            return sum_val
        
        res = float('inf')

        while i < len(nums):
            r = i
            while r < len(nums):
                cur_arr = nums[i: r + 1]
                arr_sum = calculate_sum(cur_arr)
                if arr_sum >= target:
                    
                    res = min(res, r - i + 1)
                    print(res)
                    print("r", r)
                    print("i", i)

                    break
                else:
                    r += 1
            i += 1
        if res == float('inf'):
            return 0
        else:
            return res
        





            

                

            


            
        