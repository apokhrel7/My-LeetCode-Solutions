class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # n - 2 elements are special numbers
        # 1 out of 2 elements is sum of these special numbers, other is outlier


        # place elements in dictionary to quickly find it
        dict = {}

        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1

        # total_sum = 2(sum_special_number) + outlier
        # outlier = total_sum - 2(sum_special_nums)

        total_sum = sum(nums)
        max_outlier = float('-inf')

        # for key in dict:
        #     # try each number and see if it is the sum special number
        #     outlier = total_sum - 2*key

        #     if outlier in dict.keys():
        #         if key != outlier or dict[key] > 1:
        #             max_outlier = max(max_outlier, outlier)

        for i in range(len(nums)):
            # try each number and see if it is the sum special number
            outlier = total_sum - 2*nums[i]

            if outlier in dict:
                if nums[i] != outlier or dict[nums[i]] > 1:
                    max_outlier = max(max_outlier, outlier)
            
            

        return max_outlier




        
        
