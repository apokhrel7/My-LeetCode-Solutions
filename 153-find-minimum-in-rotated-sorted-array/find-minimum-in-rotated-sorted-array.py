class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search

        # Case 1: rotated by < n (leftmost elem side bigger than rightmost)
        # Case 2: rotated by >= n (leftmost elem bigger than rightmost) 

        # 7, 0, 1, 2, 4, 5, 6
        # 6, 7, 0, 1, 2, 4, 5


        left, right = 0, len(nums) - 1
        min_elem = nums[0]

        while left <= right:
            mid = (left + right) // 2

            min_elem = min(min_elem, nums[mid])

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid - 1


        return min_elem



