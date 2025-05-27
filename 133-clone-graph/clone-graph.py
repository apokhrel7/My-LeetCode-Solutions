"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        ## DFS ##
        #  oldToNew = {}
        # def dfs(root):
        #     if root in oldToNew:
        #         return oldToNew[root]

        #     copy = Node(root.val)
        #     oldToNew[root] = copy

        #     # visit this node's neighbours
        #     for nei in root.neighbors:
        #         copy.neighbors.append(dfs(nei))

        #     # return the copy back to parent to make all the connections in both directions (undirected)
        #     return copy
        
        # return dfs(node) if node else None

        ## BFS ##
        # Base case
        if not node: return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr_node = q.popleft()

            # go through neibours of a node
            for nei in curr_node.neighbors:
                # if neighbour is not stored in hash map, then store a copy of it then add the neighbour to next in queue
                if nei not in oldToNew:
                    q.append(nei)
                    oldToNew[nei] = Node(nei.val)

                # reference the copy of the current node, and add the neighbour copy to the adjacency list
                # here we are essentially doing copied_node.neighbors.append(copied_neighbor)
                oldToNew[curr_node].neighbors.append(oldToNew[nei])

        # return head of original node
        return oldToNew[node]
                    

                



        