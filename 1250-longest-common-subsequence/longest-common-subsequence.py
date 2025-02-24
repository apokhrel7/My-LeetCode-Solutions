class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i, j):

            # if out of bounds, return 0
            if i == len(text1) or j == len(text2):
                return 0

            # if index i (for text1) and index j (for text2) already calculated, then return the cached value
            if (i, j) in cache:
                return cache[(i, j)]

            # if matching text found, then next possible LCS must be in text[i+1...n] and in text2[j+1...m]
            # Add one to cache to show that one match that satisfies LCS has been found 
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i + 1, j + 1)

            # if characters don't match for LCS, then it must be in either text[i+1...n] or in text2[j+1...m]
            # so take the biggest LCS of those two intervals 
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))


            # Here, the else statement will have finished, meaning that we have finished finding all the subproblems for an instance
            # Thus, returned the newest cached value which will contain the LCS for a certain instance (because we are always moving up incrementing i and j)
            # so the LCS is the value in cache[(i, j)]
            return cache[(i, j)]



        return dfs(0, 0)
