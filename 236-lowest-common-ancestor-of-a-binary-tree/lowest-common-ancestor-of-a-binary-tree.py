# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if both p and q are less than root, then search left subtree
        # else if both p and q are greater than root, then search right subtree
        # else, the LCA will be the root

        def dfs(node):
            if not node:
                return 

            # if p or q is found, return that node back to the parent
            if node == p or node == q:
                return node

            # keep track of the node (or assign None if no p or q found) for left and right subtree
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)

            # if we found p and q to be in opposite sides of the current root node, then that root node must be the LCA
            if left_subtree and right_subtree:
                return node
            
            # if the above if statement doesn't execute, this means that p and q are in both either in left subtree or right subtree of root
            # and one of p or q is the descendant itself
            # just return whatever isn't Null as that will be the LCA
            return left_subtree or right_subtree
    
        return dfs(root)