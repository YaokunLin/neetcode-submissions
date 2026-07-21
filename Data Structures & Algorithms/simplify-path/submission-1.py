class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
      
        for s in path:
            if s == "." or s == "":
                continue
            if s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)