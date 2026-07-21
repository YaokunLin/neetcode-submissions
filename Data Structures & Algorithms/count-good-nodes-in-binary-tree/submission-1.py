# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        count = 0
        def dfs(root, max_val):
            res = 0
            if not root:
                return 0
            if max_val  <= root.val:
                res += 1
                max_val = max(root.val, max_val)
            
            res += dfs(root.left, max_val)
            res += dfs(root.right, max_val)
            return res
        return dfs(root, root.val)
        
      
            

        

     
      
            
        