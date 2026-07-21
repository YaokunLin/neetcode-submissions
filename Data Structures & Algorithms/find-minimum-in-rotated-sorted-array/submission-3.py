class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            #left half is sorted
            if nums[mid] >= nums[l]:
                min_val = min(min_val, nums[l])
                l = mid + 1
            # right half is sorted
            else:
                min_val = min(min_val, nums[mid])
                r = mid - 1
        return min_val



        
    