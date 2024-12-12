# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        res = []

        if not root:
            return res

        q.append(root)  # add root to queue

        rightside_node = None

        while q:
            if rightside_node:
                res.append(rightside_node.val)
                
            for i in range(len(q)):
                node = q.popleft()  # leftmost node gets popped first

                if node:
                    rightside_node = node
                    q.append(node.left)  # adding left before right so that left gets popped first, right gets popped last which is when loop ends
                    q.append(node.right) 

           

        return res
        

        

            

        