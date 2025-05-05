# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use bfs
        
        def bfs(node):
            if not node: return node

            q = deque()
            q.append(node)

            new_root = node

            while q:
                q_length = len(q)
                for _ in range(q_length):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                    node.left, node.right = node.right, node.left

            return new_root


        return bfs(root)
            


