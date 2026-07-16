class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
     
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
              
            else:
                if stack:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    if token == "+":
                        res = val1 + val2
                    elif token == "-":
                        res = val2 - val1
                    elif token == "*":
                        res = val1 * val2
                    elif token == "/":
                        res = int(val2 / val1)
                    stack.append(res)
        return stack[-1]
       
 
            