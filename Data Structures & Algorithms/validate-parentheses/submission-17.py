
# stack = []
# in stack: [, (

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        close_open_map = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        stack = []
        for char in s:
            if char not in close_open_map:
                stack.append(char)
            else:
                if stack and close_open_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True


   


        

 


                

        
    
       
      