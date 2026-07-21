# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(root, cur_sum):
            if not root:
                return cur_sum
            if root.val < low:
                return dfs(root.right, cur_sum)

            if root.val > high:
               return dfs(root.left, cur_sum)

            if low <= root.val <= high:
                cur_sum += root.val
                cur_sum = dfs(root.left, cur_sum)
                cur_sum = dfs(root.right, cur_sum)
            return cur_sum
        
        return dfs(root, res)
        