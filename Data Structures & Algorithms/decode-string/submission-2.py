class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                cur_str = ""
                while stack and stack[-1] != "[":
                    cur_str = stack.pop() + cur_str
                stack.pop()
                cur_digit = ""
                while stack and stack[-1].isdigit():
                    cur_digit = stack.pop() + cur_digit
                stack.append(int(cur_digit) * cur_str)
        return "".join(stack)


            




              
            
                    

        