# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        - traverse to leftmost leaf node (gives you 1st smallest value)
        - count up from there going right
        - then going up to parent
        """
        self.count = 0
        self.theVal = 0
        def dfs(node):
            # if we reach leaf node, start counting from there so return back up
            if not node:
                return

            dfs(node.left)
            
            # left leaf node has been reached, start counting
            self.count += 1

            # return early if kth smallest is found using the count
            if k == self.count:
                self.theVal = node.val
                return

            # otherwise traverse right subtree
            dfs(node.right)

            
        dfs(root)
        return self.theVal


