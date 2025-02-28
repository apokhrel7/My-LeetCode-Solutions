class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}

        # initialize adjacency list
        for i in range(numCourses):
            adj_list[i] = []

        # populate adjacency list
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        potential_cycles = set()  # keep track of potential courses that could be cycles
        seen = set()              # keep track of courses we have already checked and verified to not be cycles


        def dfs(course):
            if course in potential_cycles:
                return False

            if course in seen:
                return True

            potential_cycles.add(course)        # this course could be a cycle, so add it to list and check

            # check cycles by going through all the prerequisites of a course
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False

            potential_cycles.remove(course)     # at this point we have verified that this course doesn't have cycles (at the moment)
            seen.add(course)                    # we have seen this course, so remember it (reduced time complexity?)

            return True


        # need to check every course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True