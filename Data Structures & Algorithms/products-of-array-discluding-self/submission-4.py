class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        prefix_arr = [1]
        for i in range(n-1):
            prefix *= nums[i]
            prefix_arr.append(prefix)
        suffix = 1
        suffix_arr = [1]
        for j in range(n - 1, 0, -1):
            suffix *= nums[j]
            suffix_arr.append(suffix)
        res = []
        print(prefix_arr)
        print(suffix_arr)
        reversed_suffix_arr = suffix_arr[::-1]
        for k in range(n):
            product = prefix_arr[k] * reversed_suffix_arr[k]
            res.append(product)
        return res






            
       
      

        