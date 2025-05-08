# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):

            # leaf node is always 0
            if not node:
                return 0

            # if node is a leaf node (found if it doesnt have any left or right children)
            # then add the value of that node + the left leaf of its right side (recurse on the right subtree of the parent)
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)

            # return the result of left and right subtree up to the parent
            # this also covers the case where a leaf node is not found yet, so recurse on left and right subtrees
            return dfs(node.left) + dfs(node.right)
            
        return dfs(root)