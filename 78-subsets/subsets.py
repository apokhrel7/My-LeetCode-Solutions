class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        def backtrack(i, temp_array):
            
            # Base Case: if all of i numbers are traversed
            if i >= n:
                res.append(temp_array.copy())   # append a deep copy of the array
                return


            # decision 1: choose ith number
            temp_array.append(nums[i])
            backtrack(i + 1, temp_array)

            # decision 2: dont choose ith number
            temp_array.pop()
            backtrack(i + 1, temp_array)

            return 

        backtrack(0, [])
        return res