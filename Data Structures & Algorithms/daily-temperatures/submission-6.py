from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        ans = [0] * len(temperatures)
        stack = deque()

        for i, t in enumerate(temperatures):
            while stack:
                last_i, last_t = stack[-1]
                if t > last_t:
                    stack.pop()
                    ans[last_i] = i - last_i
                else:
                    break
            stack.append((i, t))
        return ans


        


        
            
            


        
   
      
               

  
        