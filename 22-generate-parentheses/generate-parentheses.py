class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closedN, combo):
            if openN == closedN == n:
                res.append(combo)
                return

            if openN < n:
                dfs(openN + 1, closedN, combo + "(")

            if closedN < openN:
                dfs(openN, closedN + 1, combo + ")")

        dfs(0, 0, "")
        return res

