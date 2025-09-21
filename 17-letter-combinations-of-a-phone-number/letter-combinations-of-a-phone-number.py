class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        n = len(digits)

        def backtracking(i, curr_str):
            if len(curr_str) == n:
                res.append(curr_str)
                return
            
            for char in digits_to_letters[digits[i]]:
                backtracking(i + 1, curr_str + char)

        if not digits:
            return []
        backtracking(0, "")
        return res