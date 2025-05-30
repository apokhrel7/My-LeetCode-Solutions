class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Cycle detection on undirected graph

        adj_list = {}

        # build adjacency list
        for i in range(1, len(edges) + 1):
            adj_list[i] = []

        # populate adjacency list
        # for a, b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)


        def find_cycle(node, prev, visited):
            if node in visited:
                return True

            visited.add(node)
            for b in adj_list[node]:
                if b == prev:
                    continue
                if find_cycle(b, node, visited):
                    return True
                    
            return False

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
            if find_cycle(a, -1, set()):
                return [a, b]
        
        return []

