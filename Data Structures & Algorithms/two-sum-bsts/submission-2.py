# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(root2, remain):
            if not root2:
                return False
            if remain == root2.val:
                return True
            if remain > root2.val:
                return dfs(root2.right, remain)
            if remain < root2.val:
                return  dfs(root2.left, remain)

        def traverse(root):
            if not root:
                return False
            remain = target - root.val
            if dfs(root2, remain): 
                return True
            return traverse(root.left) or traverse(root.right)
        return traverse(root1)

        