# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # get max of left and right subtree --> return that to parent
        # but also keep track of the left + right subtrees in case root node is reached (no more parent nodes to pass recursion stack to)
        self.count = 0
        def dfs(node):
            if not node:
                return 0

            left_subtree, right_subtree = dfs(node.left), dfs(node.right)
            
            # since there can be negative nodes, keep largest of the current count or the left and right subtrees 
            self.count = max(self.count, left_subtree + right_subtree)  

            return max(left_subtree, right_subtree) + 1

        dfs(root)
        return self.count
        