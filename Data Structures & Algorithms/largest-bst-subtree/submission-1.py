class Solution:
    def largestBSTSubtree(self, root):
        self.res = 0
        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            is_subtree_left, size_left, min_left, max_left = dfs(node.left)
            is_subtree_right, size_right, min_right, max_right = dfs(node.right)
            if is_subtree_left and is_subtree_right and max_left < node.val < min_right:
                cur_size = size_left + size_right + 1
                self.res = max(self.res, cur_size)
                return True, cur_size, min(min_left, node.val), max(max_right, node.val)
            return False, 0, 0, 0
            
        dfs(root)
        return self.res
    

             
            
            
        