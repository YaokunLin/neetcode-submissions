class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s: 
            if c in char_map:
                if stack and stack[-1] == char_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
       
      