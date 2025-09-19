class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        n = len(nums)

        def backtracking(i, curr_arr, curr_sum):
            if i >= n or curr_sum > target:
                return

            if curr_sum == target:
                res.append(curr_arr.copy())
                return
            
            # keep on appending the number, 
            # recurse with new sum (curr_sum + nums[i])
            curr_arr.append(nums[i])
            backtracking(i, curr_arr, curr_sum + nums[i])

            # at this point either target reached or we overshot it
            # pop last element and try a different i to sum to
            # pass in the previous curr_sum
            curr_arr.pop()
            backtracking(i + 1, curr_arr, curr_sum)

        backtracking(0, [], 0)
        return res


            