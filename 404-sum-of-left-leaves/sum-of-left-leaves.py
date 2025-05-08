from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        # def dfs(node):
        #     if not node:
        #         return 0
        #     # if its a left leaf node
        #     # if the left node exists but that left node doesnt have left and right children, its a leaf node
        #     # hwoever, we still need to explore the right child of that node as well
        #     if node.left and not node.left.left and not node.left.right:
        #         return node.left.val + dfs(node.right)
            
        #     # if we couldn't find leaf node, recurse on the left and right subtrees
        #     return dfs(node.left) + dfs(node.right) 

           

        # return dfs(root)


        q = deque([root])
        res = 0
      
        while q:
            q_length = len(q)

           
            node = q.popleft()

            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return res

        

        