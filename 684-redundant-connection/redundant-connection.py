class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {}
        n = len(edges)
        for i in range(1, n + 1):
            adj_list[i] = []


        def dfs_is_cycle_detected(node, prev, visited):
            if node in visited:
                return True

            visited.add(node)
            for nei in adj_list[node]:
                if nei == prev:
                    continue

                if dfs_is_cycle_detected(nei, node, visited):
                    return True

            return False


        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

            if dfs_is_cycle_detected(a, b, set()):
                return [a, b]