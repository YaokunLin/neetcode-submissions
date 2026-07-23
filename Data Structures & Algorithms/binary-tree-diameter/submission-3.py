# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxHeight(root):
            if not root:
                return 0
            left = maxHeight(root.left)
            right = maxHeight(root.right)
            return 1 + max(left, right)
        
        if not root:
            return 0
        
        diameter = maxHeight(root.left) + maxHeight(root.right)

        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        
        





     


        