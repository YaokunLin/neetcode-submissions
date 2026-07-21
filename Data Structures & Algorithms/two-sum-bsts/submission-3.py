# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def search(root2, remain):
            if not root2:
                return False
            if root2.val > remain:
                return search(root2.left, remain)
            elif root2.val < remain:
                return search(root2.right, remain)
            else:
                return True
        
        def traverse(node):
            if not node:
                return False
            remain = target - node.val
            if search(root2, remain):
                return True
            return traverse(node.left) or traverse(node.right)
        return traverse(root1)
            
     

        