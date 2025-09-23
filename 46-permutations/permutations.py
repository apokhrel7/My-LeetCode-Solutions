class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        def backtrack(i, nums):
            # Base Case
            if i == len(nums):
                return [[]]

            resPerms = []
            perms = backtrack(i + 1, nums)

            for p in perms:

                # insert nums[j] into every possible
                # position in curr_arr
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])
                    resPerms.append(p_copy)
                
            return resPerms
        
        return backtrack(0, nums)