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

        ## OPTIMIZED Space-complexitty ##
        # Runtime: O(h), Space: O(k) instead of previous O(n)

        res = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            # stops recursion as soon as kth smallest element reached
            if len(res) == k:
                return
            
            res.append(node.val)
            dfs(node.right)

        
        dfs(root)
        return res[-1]


        