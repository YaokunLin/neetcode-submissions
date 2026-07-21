# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        def recursive_helper(node):
            if not node: return []
            if not node.left and not node.right:
                return [node.val]
            return recursive_helper(node.left) + [node.val] + recursive_helper(node.right)

        return recursive_helper(root)
        

 
        