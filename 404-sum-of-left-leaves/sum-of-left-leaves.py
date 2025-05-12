# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # check if left node exists and left of that left node is null and right of that left node is null
        # if above is true, then is a left leaf
        # recurse on left and right subtrees

        self.count = 0
        
        def dfs(node):
            if not node:
                return 0

            if node.left and not node.left.left and not node.left.right:
                self.count += node.left.val
            
            return dfs(node.left) + dfs(node.right)

        dfs(root)
        return self.count