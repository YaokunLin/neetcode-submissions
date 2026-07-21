class Solution:
    def checkValidString(self, s: str) -> bool:
        c_stack = []
        star_stack = []
        for i, c in enumerate(s):
            if c == "(":
                c_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            else:
                if len(c_stack) > 0:
                    c_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                elif len(c_stack) == 0 and len(star_stack) == 0:
                    return False
        while len(c_stack) > 0 and len(star_stack) > 0:
            left_index = c_stack.pop()
            star_index = star_stack.pop()
            if left_index > star_index:
                return False
        if len(c_stack) > 0:
            return False
        else:
            return True



        