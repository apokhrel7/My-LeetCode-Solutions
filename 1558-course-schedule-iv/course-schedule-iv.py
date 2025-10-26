class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        If b --> a, and
        c --> b,
        
        Then c --> b --> a.

        Prerequisites graph has NO cycles
        This solution similar to Course Schedule II but now cache the prerequisite nodes!
        """

        """

        b --> a
        c --> b

        c --> b --> a

        prerequisites graph has NO cycles
        """
        res = []
        adj_list = {c: [] for c in range(numCourses)}
        cache = [[None] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj_list[crs].append(pre)
            cache[crs][pre] = True

        def dfs(crs, target):
            # cache hit, return value stored 
            if cache[crs][target] is not None:
                return cache[crs][target]

            for pre in adj_list[crs]:

                # if we find node v from u (find that we can get prereq from a course)
                if pre == target or dfs(pre, target):
                    cache[crs][target] = True
                    return True

            # crs is not a prereq, add that to cache
            cache[crs][target] = False
            return False


        for u, v in queries:
            result = dfs(v, u)
            res.append(result)
        return res 
    