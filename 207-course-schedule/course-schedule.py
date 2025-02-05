class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1: return True
        
        
        adjList = {}

        {0: [], 1:[0]}
    

        # prepare adjacency list
        for i in range(numCourses):
            adjList[i] = []

        # add prerequisites to adjacency list
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        seen = set() # to check for cycles

        def dfs(course):
            if course in seen:
                return False

            seen.add(course)

            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            seen.remove(course)
            adjList[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        

        