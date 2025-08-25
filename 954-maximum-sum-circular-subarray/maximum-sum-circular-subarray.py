class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # res = max(res, total - globMin)

        curr_max, globMax = 0, nums[0]
        curr_min, globMin = 0, nums[0]
        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            globMax = max(globMax, curr_max)

            curr_min = min(curr_min + num, num)
            globMin = min(globMin, curr_min)

            total += num

        return globMax if globMax < 0 else max(globMax, total - globMin)