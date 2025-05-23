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
        
        q = deque([root])

        # [7]

        # 4 -> 5
        # 5 -> 6
        # 6 -> 7

        while q:
            q_length = len(q)

            for i in range(q_length):
                node = q.popleft()

                if i < (q_length - 1):
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
                
        