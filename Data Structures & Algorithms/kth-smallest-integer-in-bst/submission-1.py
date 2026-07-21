# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root, res):
            if not root:
                return
            if root:
                res.append(root.val)
          
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        
        result = dfs(root, res)
        sorted_res = sorted(result)
        print(sorted_res)
        return sorted_res[k-1]

 
    
        