from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # use bfs
        # for each level if node.right, then store it
        # for each levele, if node.right doesn't exist then store the node.left

    
        if not root: return []

        res = []
        q = deque([root])
        node = None

        while q:
            q_length = len(q)

            for _ in range(q_length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(node.val)

        return res
            
            

            
            
            
