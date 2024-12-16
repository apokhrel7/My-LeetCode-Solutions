class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # recurrence relation
        # the number of paths to get to (i, j) is the number of paths you got coming above
        # (i, j) or from the left

        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j-1]

        # d[i][j] = d[i - 1][j] + d[i][j-1]

        return dp[-1][-1]
        