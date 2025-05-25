class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        # put all numbers in hash set for quick lookup
        hash_set = set(nums)
        max_length = 0
        
        # look at an number
        # see if that number -1 exists
        # if not, then that might be the start of a sequence

        # remember to loop through the hash set not the array as the array could have all duplicates
        # this is to prevent "Time Limit Exceeded"
        for num in hash_set:
            if (num - 1) not in hash_set:
                curr_longest = 0

                while (num + curr_longest) in hash_set:
                    curr_longest += 1
                max_length = max(max_length, curr_longest)

        return max_length




        