class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for s in path:
            if s != "" and s != ".." and s != "." :
                stack.append(s)
            elif s == "." or s == "":
                continue
            elif s == ".." and stack:
                stack.pop()
        return "/"  + "/".join(stack)
  