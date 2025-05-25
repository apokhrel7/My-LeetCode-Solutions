from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        ### IDEA ###
        """
        - use BFS to go level order traversal of tree
        - connect left child to point to right child
        - do this by tracking the previous node and connect that to the right node
        - we are guaranteed that its a perfect BST
        """
        
        if not root: return root

        leftmost = root

        # since it's a perfect binary tree, we can just make sure there is a left node
        # we stop until we dont have a left node or when we hit a leaf (or right node doesnt matter)
        while leftmost.left:

            # Walk across the current level, using next pointers
            head = leftmost

            while head:
                # 1) Link head.left → head.right
                head.left.next = head.right

                # 2) If there's a next group, link head.right → head.next.left
                if head.next:
                    head.right.next = head.next.left

                # Move to the next node in this level (i.e move to right node of this current level)
                head = head.next

            # Move down one level of tree
            leftmost = leftmost.left

        return root
