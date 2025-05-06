# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # go to left subtree and count levels
        # go to right subtree and count levels

        # return max number of levels from each subtree back to parent
        # if they differ by more than 1, return False
        # return True otherwise

        def dfs(node):
            # By default, empty tree is balanced
            if not node:
                return [True, 0]

            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            isBalanced = (abs(left_subtree[1] - right_subtree[1]) <= 1) and (left_subtree[0] and right_subtree[0])

            # Pass 2 things to parent node: 
            #     1. whether its left and right subtree is balanced
            #     2. The maximum height of the child root
            return [isBalanced, max(left_subtree[1], right_subtree[1]) + 1]

        
        return dfs(root)[0]




        