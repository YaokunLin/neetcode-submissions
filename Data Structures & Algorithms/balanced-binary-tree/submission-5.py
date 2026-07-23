# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHeight(root):
            if not root:
                return 0
            left = maxHeight(root.left)
            right = maxHeight(root.right)
            return max(left, right) + 1
        if not root:
            return True
        if abs(maxHeight(root.left) - maxHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
     
       

     
     
        