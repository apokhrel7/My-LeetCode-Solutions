class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # first sort the list to get the smallest n elements in descending order 
        nums.sort()

        # [0, 0, 0, 0, 0], j =4
        # count = 3

        # get minimum value from the list and substract that to all the elements in nums
        count = 0
        j = 0
        while max(nums) > 0 and j < len(nums):
            min_element = nums[j]

            if min_element > 0:
                count += 1


                for i in range(len(nums)):
                    if nums[i] > 0:
                        nums[i] = nums[i] - min_element

            j += 1
                


        return count

