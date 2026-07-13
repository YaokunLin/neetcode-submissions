
# stack = []
# in stack: [, (

class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {
            "]": "[",
            "}":"{", 
            ")": "("
        }
        stack = []
        for char in s:
            if char not in close_map:
                stack.append(char)
            else:
                if stack and close_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        


   


        

 


                

        
    
       
      