class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        potential_cycles = set()
        visited = set()

        def dfs(node):
            if node in potential_cycles:
                return False

            if node in visited:
                return True

            potential_cycles.add(node)            
            for pre in adj_list[node]:
                if not dfs(pre):
                    return False
                    
            visited.add(node)
            potential_cycles.remove(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res