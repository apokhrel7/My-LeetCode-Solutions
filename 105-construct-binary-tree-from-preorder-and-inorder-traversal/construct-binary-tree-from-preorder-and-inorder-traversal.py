# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        # root is first element of preorder
        root = TreeNode(preorder[0])

        # track where root is in preorder (left of that root is left subtree, right of that root is right subtree)
        mid = inorder.index(preorder[0])

        # root of left subtree is from 1...m, left childrren are from 0...mid
        root.left = self.buildTree(preorder[1: mid + 1], inorder[: mid])

        # root of right subtree is from mid + 1...n, right childrren are from mid+1...n
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])

        return root