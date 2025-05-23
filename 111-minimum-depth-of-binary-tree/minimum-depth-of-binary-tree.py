from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #### DFS ####

        # if not root:
        #     return 0

        # # if leaf node found, return the first depth
        # if not root.left and not root.right:
        #     return 1

        # # if only left subtree has children, recurse on the left child
        # if root.left and not root.right:
        #     return self.minDepth(root.left) + 1

        # # recurse on right subtree
        # if root.right and not root.left:
        #     return self.minDepth(root.right) + 1

        # # if both left and right children exist, recurse on both and return the minimum depth
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


        #### BFS ####
        if not root: return 0

        q = deque([root])
        min_depth = 1  # since we have a root, start with depth as 1
        
        while q:

            # take snapshot of length of queue since we are doing BFS (level by level)
            q_length = len(q)
            for _ in range(q_length):
                node = q.popleft()

                if not node.left and not node.right:
                    return min_depth
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # at this point, we have gone through a level in the tree
            min_depth += 1
        
        return min_depth