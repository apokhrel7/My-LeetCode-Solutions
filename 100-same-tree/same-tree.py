# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_, q_):
            # if both are leaf nodes --> identical in structure
            if not p_ and not q_:
                return True

            # if one of the nodes is Null and the other isn't --> not identical in structure
            if not p_ or not q_:
                return False

            # last check if the value of each node is the same and recurse on left and right substrees
            return q_.val == p_.val and dfs(p_.left, q_.left) and dfs(p_.right, q_.right)

        
        return dfs(p, q)

        