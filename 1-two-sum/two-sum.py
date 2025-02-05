class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create hash table

        # hashed_nums = {}
            


        # difference = 0
        # for i in range(len(nums)):


        #     difference = target - nums[i]

        #     if difference in hashed_nums and hashed_nums[difference] != i :
        #         return [i, hashed_nums[difference]]
        #     hashed_nums[nums[i]] = i


        # return []

        dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dict:
                return [i, dict[complement]]

            
            dict[nums[i]] = i

        return []


                    
                    
        
        