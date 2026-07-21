class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = set()
        for i in range(len(numbers)):
            remain = target - numbers[i]
            if remain in visited:
                return [numbers.index(remain) + 1, i + 1]
            else:
                visited.add(numbers[i])
                

      
     

        
     
        