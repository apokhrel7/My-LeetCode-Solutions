# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def dfs(node, count):
            
            # leaf node will initially always return False
            if not node:
                return False

            # keep track of the sum at each tree level
            count += node.val

            # go all the way to leaf node and now check if the current count is the target
            # If yes, return true 
            if node and not node.left and not node.right:
                return count == targetSum
            
            # recurse on left and right subtrees, keeping track of the sum
            return dfs(node.left, count) or dfs(node.right, count)

        return dfs(root, 0)
