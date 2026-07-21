# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            left_dept = dfs(node.left)
            right_dept = dfs(node.right)
            current_diameter = left_dept + right_dept
            self.res = max(self.res, current_diameter)
            return max(left_dept, right_dept) + 1
        dfs(root)
        return self.res


        