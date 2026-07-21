class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        target = n - k

        def quickSelect(arr, index):
            pivot = arr[len(arr) // 2]
            lows = [num for num in arr if num < pivot]
            mid = [num for num in arr if num == pivot]
            highs = [num for num in arr if num > pivot]
            if index < len(lows):
                return quickSelect(lows, index)
            elif index < len(lows) + len(mid):
                return pivot
            elif len(lows) + len(mid) <= index < len(arr):
                return quickSelect(highs, index - len(lows) - len(mid))

        return quickSelect(nums, target)