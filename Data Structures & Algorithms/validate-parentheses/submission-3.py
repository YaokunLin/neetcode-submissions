class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char not in s_map:
                stack.append(char)
            else:
                if stack and stack[-1] == s_map[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
                

        
    
       
      