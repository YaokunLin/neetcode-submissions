class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level):
            if not node:
                return
            # If this is the first node we're visiting at this level,
            # it is the rightmost node we've seen so far at this level.
            if level == len(res):
                res.append(node.val)
            # First traverse the right subtree, then the left subtree.
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        res = []
        dfs(root, 0)
        return res
