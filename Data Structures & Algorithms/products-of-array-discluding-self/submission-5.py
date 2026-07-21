class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def get_product(arr, index):
            product = 1
            for i in range(len(arr)):
                if i != index:
                    product *= arr[i]
            return product
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = get_product(nums, i)
        return res

        






            
       
      

        