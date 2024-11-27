class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)
        def dfs(i, curr_sum, sub_array):

            # Base Case 1: if out of bounds or current sum overshoots the target 
            if i > n - 1 or curr_sum > target:
                return

            # Base Case 2: if chosen numbers sum to target, append that combination to resulting array
            if curr_sum == target:
                res.append(sub_array.copy())
                return 

            # As long as base cases don't execute, add numbers to sub list
            sub_array.append(candidates[i])

            # keep summing up the ith number (ex. 2+ 2 + 2)
            dfs(i, curr_sum + candidates[i], sub_array)

            # once ith number has been tested and summed, pop from sub list and try summing up next number in candidates list (i + 1)
            sub_array.pop()  # first remove, the ith number from sub list
            dfs(i + 1, curr_sum, sub_array) 

            return

        dfs(0, 0, [])
        return res
            
        
