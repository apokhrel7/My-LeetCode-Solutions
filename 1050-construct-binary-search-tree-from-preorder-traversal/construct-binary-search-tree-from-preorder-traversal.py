# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # If list is empty, this means leaf node so return Null
        if not preorder:
            return None

        # root will always be the first element
        root = TreeNode(preorder[0])

        # since it's a BST, we can find all nodes from left subtree
        i = 1
        while i < len(preorder) and root.val > preorder[i]:
            i += 1

        # at this point, "i - 1" will tell give us a range of all the left children (don't include root)
        root.left = self.bstFromPreorder(preorder[1:i])

        # right children will be i...n
        root.right = self.bstFromPreorder(preorder[i:])

        return root


        