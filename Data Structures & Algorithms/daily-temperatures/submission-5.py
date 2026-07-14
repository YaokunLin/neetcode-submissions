class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                old_i = stack.pop()
                days = i - old_i
                res[old_i] = days
            stack.append(i)
        return res


        
            
            


        
   
      
               

  
        