class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}

        res = []


        # initialize
        for i in range(numCourses):
            preMap[i] = []

        # append
        for pre, crs in prerequisites:
            preMap[pre].append(crs)


        potential_cycles = set()
        seen = set()
        def dfs(course):
            if course in potential_cycles:
                return False

            if course in seen:
                return True

            potential_cycles.add(course)            
            for pre in preMap[course]:
                if not dfs(pre): return False

            seen.add(course)
            potential_cycles.remove(course)  # can be ruled out as cycle
            res.append(course)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res