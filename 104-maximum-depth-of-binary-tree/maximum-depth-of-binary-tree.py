from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # def dfs(node):
        #     if not node:
        #         return 0

        #     return max(dfs(node.left), dfs(node.right)) + 1


        # return dfs(root)

        if not root: return 0
        q = deque([root])
        res = 0

        while q:
            q_length = len(q)

            for _ in range(q_length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += 1
        return res



        