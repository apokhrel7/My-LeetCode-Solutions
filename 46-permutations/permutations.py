class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)


        def backtrack(i):
            if i == n:
                return [[]]

            res_perms = []
            curr_perms = backtrack(i + 1)

            for p in curr_perms:

                # insert nums[i] into every possible position 
                # in a current permutation
                for j in range(len(p) + 1):
                    p_copy = p.copy()  # can also use p[::] ?
                    p_copy.insert(j, nums[i])
                    res_perms.append(p_copy)

            return res_perms

        return backtrack(0)
