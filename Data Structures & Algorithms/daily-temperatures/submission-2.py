class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temp, pos = stack.pop()
                res[pos] = index - pos
            stack.append((val, index))
        return res
            
            


        
   
      
               

  
        