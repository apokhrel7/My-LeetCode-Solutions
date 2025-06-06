from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # def dfs(node):
        #     if not node:
        #         return None

        #     if node.val == val:
        #         return node

        #     if node.val < val:
        #         return dfs(node.right)

        #     return dfs(node.left)

        # return dfs(root)

        ## BFS QUEUE ##
        # q = deque([root])

        # while q:
        #     node = q.popleft()

        #     if not node:
        #         return None

        #     elif node.val == val:
        #         return node

        #     elif node.val < val:
        #         q.append(node.right)
            
        #     else:
        #         q.append(node.left)

        # return None


        ### WITHOUT QUEUE ###
        node = root

        while node:
            if node.val == val:
                return node
            elif node.val < val:
                node = node.right
            else:
                node = node.left

        return None