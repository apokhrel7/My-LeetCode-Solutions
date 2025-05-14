# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     # check if tree is the same
    def isSameTree(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False

        return r.val == s.val and self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # if subroot is empty, no need to check further, return True
        if not subRoot: 
            return True
        
        # at this point, subRoot is not empty but root is empty
        # clearly subroot isn't a real subroot so return False
        if not root:
            return False
        # if it's the same tree, return True
        if self.isSameTree(root, subRoot):
            return True

        # if not same tree, then recurse on left and right subtrees, and take whichever branch
        # subtree could be in either left OR right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 



   





        