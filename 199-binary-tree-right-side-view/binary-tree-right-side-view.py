# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # need to traverse level by level --> 
        res = []

        if not root: return res
        
        q = deque()
        q.append(root)
        right_side_node = None

        while q:
            
            n = len(q)

            for _ in range(n):
                right_side_node = q.popleft()
                
                if right_side_node.left:
                    q.append(right_side_node.left)

                if right_side_node.right:
                    q.append(right_side_node.right)

            
            res.append(right_side_node.val)

        return res

        

            

        