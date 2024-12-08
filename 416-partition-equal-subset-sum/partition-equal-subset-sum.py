class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # at each tree level: n choices

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        def dfs(i, sum_, cache):

            # case 1: out of bounds, case 2: sum is too large
            if i >= n or sum_ > target:
                return False

            # case 3: subset sum is found
            if sum_ == target:
                return True

            # case 4: if subproblem has already been solved
            if (i, sum_) in cache:
                return cache[(i, sum_)]

            # store the sum problem within pair (i, sum) representing sum at index i by either including nums[i] or not including it
            cache[(i, sum_)] = dfs(i + 1, nums[i] + sum_, cache) or dfs(i + 1, sum_, cache)
            return cache[(i, sum_)]
            

           

        return dfs(0, 0, {})

        