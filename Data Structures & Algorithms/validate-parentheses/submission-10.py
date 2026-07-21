
# stack = []
# in stack: [, (

class Solution:
    def isValid(self, s: str) -> bool:

        open_to_close = {
            '(' : ')', 
            '{' : '}', 
            '[' : ']'
        }

        opens = open_to_close.keys()
        closes = open_to_close.values()

        stack = []

        for p in s:
            if p in opens:
                stack.append(p)
            else:
                # p is a close
                if stack:
                    last_open = stack.pop()
                    needed_close = open_to_close[last_open]
                    if p != needed_close:
                        return False 
                else:
                    # there is a close but there is no matching open
                    return False
        return len(stack) == 0


        

 


                

        
    
       
      