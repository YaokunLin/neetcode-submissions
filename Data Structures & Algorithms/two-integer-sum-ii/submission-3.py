class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l <= r:
            
            if numbers[l] + numbers[r] > target:
                # right number is too big
                r = r - 1
            elif numbers[l] + numbers[r] < target:
                # left number is too small
                l = l + 1
            else:
                return [l+1, r+1]
     

        
     
        