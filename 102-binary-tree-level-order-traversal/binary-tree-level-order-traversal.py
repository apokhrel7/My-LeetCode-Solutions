from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS traversal
        if not root: return []
        
        res = []
        q = deque([root])

        while q:
            q_length = len(q)
            temp_arr = []
            for _ in range(q_length):
                node = q.popleft()
                temp_arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(temp_arr)
        return res