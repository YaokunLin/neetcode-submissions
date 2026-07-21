class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            left = target - num
            if left not in visited:
                visited[num] = i
            else:
                return [visited[left], i]

        