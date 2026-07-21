class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l < len(numbers):
            r = l + 1
            while r < len(numbers):
                if numbers[r] + numbers[l] != target:
                    r = r + 1
                else:
                    return [l + 1, r + 1]
            l = l + 1
        