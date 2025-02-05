class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # use set() to get all distinct elements

        # distinct_elements = set(nums)

        # to_get_rid_of = len(nums) - distinct_elements

        # if to_get_rid_of % 3
        # (1, 2, 3, 4, 5, 7)

        # 9-6 = 3
        # [2, 3, 3]

        # (4, 5, 6)
        # 5 - 3 = 2
        # [4, 4]

        # return len(distinct_elements) // 2

        count = 0
        i = 0
        while len(nums) > 0:
            if len(nums) == len(set(nums)):
                return count
            del nums[:3]
            

            count += 1

        return count