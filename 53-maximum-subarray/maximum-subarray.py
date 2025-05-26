class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        - Greedy 
        - two choices when at an element i
        - include i in the subarray list or dont include it (include i + 1 instead)
        - decide this by calculating the current maximum 
        """
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        max_sum = prev
        for num in nums[1:]:
            curr = max(num + prev, num)
            prev = curr
            max_sum = max(max_sum, curr)

        return max_sum



