# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder_dfs(node):
            if not node: return 
            
            res.append(node.val)
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)
        return res