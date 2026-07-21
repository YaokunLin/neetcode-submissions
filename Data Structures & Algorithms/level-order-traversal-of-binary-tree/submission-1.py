# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        level = 0
        if root:
            queue.append(root)
        while len(queue) > 0:
            res_sub = []
            for i in range(len(queue)):
                curr = queue.popleft()
                res_sub.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(res_sub)
        return res

   
            
        