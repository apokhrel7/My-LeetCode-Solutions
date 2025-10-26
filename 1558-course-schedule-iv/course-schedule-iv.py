class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        If b --> a, and
        c --> b,
        
        Then c --> b --> a.

        Prerequisites graph has NO cycles
        This solution similar to Course Schedule II but now cache the prerequisite nodes!
        """

        res = []
        adj_list = {c: [] for c in range(numCourses)}

        for pre, crs in prerequisites:
            adj_list[crs].append(pre)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()

                for pre in adj_list[crs]:
                    # prereqMap[crs].update(dfs(pre)) # this equivalent
                    prereqMap[crs] |= dfs(pre)

                # at the end, add course itself as prereq
                prereqMap[crs].add(crs)

            # crs is indirect or direct prereq
            return prereqMap[crs]

        # populate the prereqMap
        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        # Check the queries and if u is in the prereq map we computed
        # This way we cache all prereqs to make it more efficient and prevent recursing
        # nodes we already visited
        for u, v in queries:
            result = u in prereqMap[v]
            res.append(result)
        return res 
    