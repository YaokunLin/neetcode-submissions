class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        n = len(nums)
        mid = n // 2
        if len(nums) <= 1:
            return nums
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        # merge two
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left) and j >= len(right):
            res.append(left[i])
            i += 1
        while j < len(right) and i >= len(left):
            res.append(right[j])
            j += 1

        return res





 