class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # keep track of borders

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        TOTAL_ELEMENTS = len(matrix) * len(matrix[0])
        res = []

        while top < bottom and left < right:
            # go from left to right
            for col in range(left, right):
                res.append(matrix[top][col])

            # go from up to down
            for row in range(top, bottom):
                res.append(matrix[row][right])

            print(res)
            # go from right to left
            for col in range(right, left, -1):
                res.append(matrix[bottom][col])

            # go from down to up
            for row in range(bottom, top, -1):
                res.append(matrix[row][left])

            # decrease size of borders
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # at this point, if there are still elements to be added, it must be a 1d matrix now
        # add the remaining parts
        if len(res) < TOTAL_ELEMENTS:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    res.append(matrix[row][col])
        return res