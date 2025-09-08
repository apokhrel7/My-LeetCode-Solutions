class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find local minima
        # track local max using the local minima number
        # update max

        if len(nums) == 0:
            return 0

        hash_set = set(nums)

        global_max_length = 0

        for num in hash_set:
            
            # this could be the beginning of the sequence
            # since there's no sequence before it
            if (num - 1) not in hash_set:
                curr_length = 1

                while (num + curr_length) in hash_set:
                    curr_length += 1

                global_max_length = max(global_max_length, curr_length)

        return global_max_length
