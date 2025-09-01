class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Keep track of prefix sum
        # Keep track of hashmap of prefix sums to see how many of them exist
        # diff = curr_prefix_sum - k gives us a number that if removed, gives us a subarray adding to k
        # check if that diff is in hashmap, add the total number of occurances of that diff into result

        res, curr_sum = 0, 0
        prefix_hashmap = {0: 1}

        for num in nums:
            curr_sum += num

            diff = curr_sum - k

            # the below is written as:
            # if diff in prefix_hashmap:
            #     res += prefix_hashmap[diff]

            res += prefix_hashmap.get(diff, 0)

            prefix_hashmap[curr_sum] = prefix_hashmap.get(curr_sum, 0) + 1

        return res
