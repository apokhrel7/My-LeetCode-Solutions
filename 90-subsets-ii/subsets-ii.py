class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        def backtracking(i, curr_stack):
            if i >= n:
                # turn into tuple and add to set
                res.add(tuple(curr_stack))
                return

            # include i
            curr_stack.append(nums[i])
            backtracking(i + 1, curr_stack, )

            # don't include i
            curr_stack.pop()
            backtracking(i + 1, curr_stack)

        nums.sort() # numbers must be in sorted order to prevent duplicates
        backtracking(0, [])

        res2 = []

        # put tuple collections into list
        for t in res:
            res2.append(list(t))
        return res2