class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        print(path)
        for s in path:
            if stack and s == "..":
                stack.pop()
            elif s != "." and s !="" and s != "..":
                stack.append(s)
        return "/" + "/".join(stack)