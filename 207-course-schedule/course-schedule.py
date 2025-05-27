class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        # adj_list = {0: [], 1: [0]}

        # create adjacency list
        for i in range(numCourses):
            adj_list[i] = []

        # populate adjacency_list
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        potential_cycle = set()  # track courses that could be potential cycles
        visited = set()          # track courses that you have already seen, this increases efficiency as we don't have to check courses we have already visited for cycles

        def dfs(crs):

            # Base case 1: if cyclical refernce to same course detected (cycle detected), return False
            if crs in potential_cycle:
                return False

            # if we are visiting a course again but there is no cycle, return True
            if crs in visited:
                return True

            # new unseen course, so add it to a set of potential cycles
            potential_cycle.add(crs)

            # go through the neigbours of this node and recurse on them to detect cycles
            for pre in adj_list[crs]:
                if not dfs(pre): 
                    return False

            # at this point, no cycles detected for this course so remove it from list of potential cycles
            potential_cycle.remove(crs)
            
            # remember this course as we have checked it for cycles
            visited.add(crs)
            return True  # at this point, everything is looking good, return True

        # we have to run this cycle detection for every course
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
