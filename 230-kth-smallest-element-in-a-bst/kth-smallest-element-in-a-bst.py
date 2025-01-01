# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse left first, then right
        # count how many times to come up to parent

        # just add nodes to list until it reaches k elements so return last one

        res = []
        def dfs(node):
            if not node:
                return

            if len(res) == k:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        
        dfs(root)
        return res[k-1]


        