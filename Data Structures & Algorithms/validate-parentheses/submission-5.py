class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for c in s:
            if c not in s_map:
                stack.append(c)
               
            else:
                if stack and stack[-1] == s_map[c]:
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        else:
            return True


                

        
    
       
      