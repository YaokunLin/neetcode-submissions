# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(root, close_node):
            if not root:
                return close_node
            cur_diff = abs(root.val - target)
            close_diff = abs(close_node - target)
            if close_diff >= cur_diff:
                close_node = root.val
            else:
                close_node = close_node
            close_node = dfs(root.left, close_node)
            close_node = dfs(root.right, close_node)
            return close_node
        return dfs(root, root.val)

        