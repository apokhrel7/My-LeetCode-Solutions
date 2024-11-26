class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target:
                return pivot

            # left half of array is sorted
            elif nums[pivot] >= nums[left]:
                if target < nums[left] or target > nums[pivot] :
                    left = pivot + 1
                else:
                    right = pivot - 1

            # right half of array is sorted
            else:
                if target > nums[right] or target < nums[pivot]  :
                    right = pivot - 1
                else:
                    left = pivot + 1 

        
        return -1