class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {}
        res = []
        potential_cycle = set()
        visited = set()

        # initialize adjacency list
        for i in range(numCourses):
            adj_list[i] = []

        # populate adjacency list
        for pre, course in prerequisites:
            adj_list[pre].append(course)

        def dfs(crs):
            if crs in visited:
                return True

            if crs in potential_cycle:
                return False

            potential_cycle.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre): return False
            
            potential_cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
            
        return res