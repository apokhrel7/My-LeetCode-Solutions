# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # recursive (dfs) solution using left and right node value boundries

        def dfs(node, left_boundary, right_boundary):

            # if leaf node is reached, return True as we haven't broken definition of BST
            if not node:
                return True

            # not a BST, return False
            if not (left_boundary < node.val < right_boundary):
                return False

            ### Recurse on left and right subtrees ###

            # left subtree can only have values less than its parent (update right_boundary = val of parent node) 
            # right subtree can only have values greater than its parent (update left_boundary = val of parent node) 

            return dfs(node.left, left_boundary, node.val) and dfs(node.right, node.val, right_boundary)


        # initialy root is bounded by -inf < root.val < inf (root can be any value)
        return dfs(root, float('-inf'), float('inf'))  



            
