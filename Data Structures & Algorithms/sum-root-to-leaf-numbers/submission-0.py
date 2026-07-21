# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, root.val)])
        res = 0
        while q:
            node, num = q.popleft()
            if not node.left and not node.right:
                res += num
            if node.left:
                q.append((node.left, num * 10 + node.left.val))
            if node.right:
                q.append((node.right, num * 10 + node.right.val))
            
        return res

                
