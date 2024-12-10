class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(temp, i):
            # pick i or don't pick it

            # base case, when i is out of bounds
            if i >= len(nums):
                res.append(temp.copy())
                return

            # pick nums[i]
            temp.append(nums[i])
            dfs(temp, i + 1)

            # don't pick nums[i], pop it out the list and pick something else
            temp.pop()
            dfs(temp, i + 1)



        dfs([], 0)
        return res