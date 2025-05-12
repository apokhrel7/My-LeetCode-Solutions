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
        
        def dfs(node):
            if not node:
                return 0

            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)  # explore right subtree of this node as it could have left leaves
            
            return dfs(node.left) + dfs(node.right)

        return dfs(root)
        