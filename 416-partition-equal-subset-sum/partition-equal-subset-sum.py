class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dfs with cache
        # Case 1: include ith element
        # Case 2: don't include ith element
        # recurse + cache

        # if sum not divisible by 2, can't partition into two subsets
        if sum(nums) % 2 != 0: return False

        n = len(nums)

        # this is what we're trying to reach
        target_sum = sum(nums) // 2

        cache = {}


        def dfs(i, curr_sum):
            
            # Base case 1: i out of bounds
            # Base case 2: sum we calculate overshoots the target
            if i >= n or curr_sum > target_sum:
                return False

            if curr_sum == target_sum:
                return True

            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            
            cache[(i, curr_sum)] = dfs(i + 1, curr_sum) or dfs(i + 1, curr_sum + nums[i]) 
            # # include ith element
            # dfs(i + 1, nums[i])

            # # don't include ith element
            # dfs(i + 1)

            return cache[(i, curr_sum)]


        return dfs(0, 0)



        