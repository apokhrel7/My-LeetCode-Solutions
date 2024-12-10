class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        target_num = sum(nums) // 2

        # Base case 1
        if sum(nums) % 2 != 0:
            return False

        
        def dfs(i, sum_, cache):
            # Base case 2, 3
            if i >= n or sum_ > target_num:
                return False

            # Base case 4
            if sum_ == target_num:
                return True

            if (i, sum_) in cache:
                return cache[(i, sum_)]

            cache[(i, sum_)] = dfs(i + 1, nums[i] + sum_, cache) or dfs(i + 1, sum_, cache)
            return cache[(i, sum_)]

        return dfs(0, 0, {})


        