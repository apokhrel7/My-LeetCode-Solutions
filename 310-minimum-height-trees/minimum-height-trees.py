from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # first build adjacency list of the edges
        
        # Base Case: if theres only 1 node (labelled node "0"), then that node is the MHT's root
        if n == 1:
            return [0]
        

        adj_list = {}
        outgoing_edges = []

        # initialize empty adjacency list
        for i in range(n):
            adj_list[i] = []

        for incoming, outgoing in edges:
            adj_list[incoming].append(outgoing)
            adj_list[outgoing].append(incoming)


        edge_count = {}
        leaves = deque()
        
        # count edges and find leaf nodes
        for incoming, outgoing in adj_list.items():
            edge_count[incoming] = len(outgoing)

            if edge_count[incoming] == 1:
                leaves.append(incoming)


        # adj_list = {0: [1], 1: [0, 2, 3], 2: [1], 3: [1] }
        # edge_count = {0: 1, 1: 3, 2: 1, 3: 1}
        # leaves = [0, 2, 3]

        # start deleting leaves, return whatever is remaining after there is only 1 or 2 nodes left (return those nodes that are left)
        while leaves:

            ### IMPORTANT INSIGHT: if total nodes are 1 or 2, those are the MHT's roots ###
            if n <= 2:
                return list(leaves)

            snapshot_leaves = len(leaves)

            for i in range(snapshot_leaves):
                node = leaves.popleft()

                # decrement total number of nodes
                n -= 1

                # update neighbours of deleted nodes
                for neighbours in adj_list[node]:
                    edge_count[neighbours] -= 1

                    # neighbour of the node we just deleted might have become a leaf node, so check for this and add to leaves queue
                    if edge_count[neighbours] == 1:
                        leaves.append(neighbours)


            

        

        



        
        