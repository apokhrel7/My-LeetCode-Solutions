class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # create hashmap/dictionary of digits to their corresponding letters

        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        n = len(digits)
        def backtracking(i, curr_string):
            # once all the digits have been traversed, add the combination to resulting list and return
            if i >= n:
                res.append(curr_string)
                return

            # go through each mappiong of digits to letters, going to each ith digit as well
            for digit in digits_to_letters[digits[i]]:
                backtracking(i + 1, curr_string + digit)   # combine i with i + 1, also combining the strings with each letter

        # if digits is non-empty, then run backtracking algorithm
        if digits:
            backtracking(0, "")
        return res


        
        