class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # at each tree level: n choices

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        def dfs(i, sum_, cache):

            # case 1: out of bounds
            if i >= n:
                return False

            # case 2: sum is too large
            if sum_ > target:
                return False

            # case 3: subset sum is found
            if sum_ == target:
                return True

            if (i, sum_) in cache:
                return cache[(i, sum_)]


            cache[(i, sum_)] = dfs(i + 1, nums[i] + sum_, cache) or dfs(i + 1, sum_, cache)
            return cache[(i, sum_)]
            

           

        return dfs(0, 0, {})

        