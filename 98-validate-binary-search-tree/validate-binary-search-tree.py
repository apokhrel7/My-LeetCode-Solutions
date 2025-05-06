# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # -inf < node < +inf
        def dfs(node, left_boundary, right_boundary):
            # Leaf node is considered a valid BST
            if not node:
                return True

            # if the left subtree is not less than node's key or right_substree is not greater than node's key: return false
            if not (left_boundary < node.val < right_boundary):
                return False

            # go left subtree and right subtree
            # when traversing left subtree, boundary becomes -inf < node.left.val < node.val
            # when traversing right subtree, boundary becomes node.val < node.right.val < +inf
            return dfs(node.left, left_boundary, node.val) and dfs(node.right, node.val, right_boundary)

        

        return dfs(root, float("-inf"), float("inf"))

        