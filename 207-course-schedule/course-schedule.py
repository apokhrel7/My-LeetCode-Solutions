class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}

        {1:[0], 0:[]}

        # initialize
        for i in range(numCourses):
            preMap[i] = []

        # append
        for pre, crs in prerequisites:
            preMap[pre].append(crs)


        potential_cycles = set()
        def dfs(course):
            if course in potential_cycles:
                return False
            
            # leaf node: return True
            if not preMap[course]:
                return True

            potential_cycles.add(course)

            for pre in preMap[course]:
                if not dfs(pre): return False
            
            potential_cycles.remove(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        


        
