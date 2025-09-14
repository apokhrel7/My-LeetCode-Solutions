from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""Flatten the BST - Iterative"""
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        curr = root
        stack = []
        self.nodes = deque([])  # double-ended queue to get FIFO (first in, first out for next() function)

        while curr or stack:
            # go through left subtree first
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            self.nodes.append(curr)
            curr = curr.right

    def next(self) -> int:
        return self.nodes.popleft().val  # pop the first elements out

    def hasNext(self) -> bool:
        return len(self.nodes) > 0  # If has elements --> True, Otherwise False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
