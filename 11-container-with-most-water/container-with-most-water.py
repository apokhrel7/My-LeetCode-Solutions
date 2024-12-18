class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # initialize left and right, record max container amount
        # if left line < right line: move left line up
        # else: move right line up 

        left, right = 0, len(height) - 1

        max_area = 0

        # repeat until there are no more two lines that can hold water between them
        while left < right:

            # area is the distance between leftmost and rightmost lines times the smallest height of among them 
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            # move left pointer up if left line is smaller than right line
            if height[left] < height[right]:
                left += 1

            # otherwise move right pointer as right line is smaller than left
            else:
                right -= 1

        return max_area


