class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        # offset row and col by 1 more to add 0s for first row, first column
        self.prefix_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            pref_col = 0
            for col in range(COLS):
                pref_col += matrix[row][col]

                above_row = self.prefix_matrix[row][col + 1]
                # prefix_matrix[row][col] = pref_row + above
                self.prefix_matrix[row + 1][col + 1] = pref_col + above_row

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Apply offsets to row and col
        row1 += 1
        col1 += 1

        row2 += 1
        col2 += 1

        # this is confusing, make sure to draw it out
        # sum_range = bottom_right - left - top + top_left

        # must add top left because we are removing it twice (only need to remove it once)
        # as we are removing rows from left to right above (r1-1, c2) and top to bottom (r2, c1-1)
        bottom_right = self.prefix_matrix[row2][col2]
        left = self.prefix_matrix[row2][col1 - 1]
        top = self.prefix_matrix[row1 - 1][col2]
        top_left = self.prefix_matrix[row1 - 1][col1 - 1]

        return bottom_right - left - top + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
