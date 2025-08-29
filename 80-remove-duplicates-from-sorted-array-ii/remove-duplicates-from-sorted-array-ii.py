class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # just care about 2 numbers
        
        l = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[l-2]:
                nums[l] = nums[i]
                l += 1

        return l

        