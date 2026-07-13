class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                while stack and stack[-1] > 0:

                    if stack and stack[-1] == -ast:
                        stack.pop()
                        break
                    elif stack and stack[-1] > -ast:
                        break
                    elif stack and stack[-1] < -ast:
                        stack.pop()
                else:
                    stack.append(ast)

        return stack
   
     
        