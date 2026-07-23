# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        copy = root
        left_temp = copy.left
        right_temp = copy.right
        copy.left = self.invertTree(right_temp)
        copy.right = self.invertTree(left_temp)
        return copy


        
   

        
        
        