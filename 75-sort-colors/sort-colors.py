class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Use insertion sort

        # p0, p1 = 0, 1
        # n = len(nums)

        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]


        ### Use hashmap and bucket sort ###
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        # dict = {2: 2, 0: 2, 1: 2}
        start = 0
        for i in range(3):
            if i in dict:
                nums[start : start + dict[i]] = [i] * dict[i]
                start += dict[i]

        

         