class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, val in enumerate(nums):
            remaining = target - val
            if remaining not in visited:
                visited[val] = i
            else:
                return [visited[remaining], i]
            
  


        

        