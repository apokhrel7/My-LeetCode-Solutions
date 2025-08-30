class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array = []
        total = 0

        for num in nums:
            total += num
            self.prefix_array.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        # prefix right - prefix (left - 1)
        prefix_right = self.prefix_array[right]

        # only if left is not last element, otherwise prefix left is 0
        prefix_left = self.prefix_array[left - 1] if left > 0 else 0 

        return (prefix_right - prefix_left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)