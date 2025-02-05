class Solution:
    def rob(self, nums: List[int]) -> int:
        # recurrence relation
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # if len(nums) == 1: return nums[0]
        # dp = [0] * len(nums)
        # # Base cases
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # return dp[-1]

        # we don't need to store whole array, just need previous values

        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        # Base cases
        max_robber = 0
        prev_max_robber = 0
     

        for i in range(len(nums)):
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            temp = max(prev_max_robber + nums[i], max_robber)
            prev_max_robber = max_robber
            max_robber = temp
            


        return max_robber


        