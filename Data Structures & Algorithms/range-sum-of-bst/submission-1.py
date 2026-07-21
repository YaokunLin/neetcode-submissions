# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        stack = [root]
        while stack:
            cur_root = stack.pop()
            if not cur_root:
                continue
            if cur_root.val < low:
                stack.append(cur_root.right)
            elif cur_root.val > high:
                stack.append(cur_root.left)
            else:
                res += cur_root.val
                stack.append(cur_root.left)
                stack.append(cur_root.right)
                
        return res
      
        