# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            left_dept = dfs(root.left)
            right_dept = dfs(root.right)
            current_diameter = left_dept + right_dept
            self.res = max(self.res, current_diameter)
            return max(left_dept, right_dept) + 1
        dfs(root)
        return self.res


        