# []()
# [()]
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        if len(s) % 2 == 1: return False

        close_to_open = {
             ')' : '(', 
             '}' : '{', 
             ']' : '['
        }

        opens = close_to_open.values()
        closes = close_to_open.keys()
        stacked_opens = []

        for c in s:
            if c in opens:
                stacked_opens.append(c)
            else:
                # now, c is a close
                if not stacked_opens:
                    # there is a close, but no corresponding opens in stack
                    return False 
                last_open = stacked_opens.pop(-1)
                needed_open = close_to_open[c]
                if last_open != needed_open:
                    return False
        return True if not stacked_opens else False
 


                

        
    
       
      