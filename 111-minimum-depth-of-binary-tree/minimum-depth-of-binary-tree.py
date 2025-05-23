# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if leaf node found, return the first depth
        if not root.left and not root.right:
            return 1

        # if only left subtree has children, recurse on the left child
        if root.left and not root.right:
            return self.minDepth(root.left) + 1

        # recurse on right subtree
        if root.right and not root.left:
            return self.minDepth(root.right) + 1

        # if both left and right children exist, recurse on both and return the minimum depth
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

