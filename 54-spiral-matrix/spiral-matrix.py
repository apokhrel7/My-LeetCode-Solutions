class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # go right, go down, go left, go up, repeat...
        # update left, right, up, and down borders at the end
        
        # Edge case:
        # there will be a case where only a 1d array is left (either 1 column and many rows, or 1 row and many columns),
        # then just traverse that normally as you would in a 1d array

        TOTAL_ELEMENTS = len(matrix) * len(matrix[0]) 

        right_border, left_border = len(matrix[0]) - 1, 0
        top_border, bottom_border = 0, len(matrix) - 1 

        res = []

        while left_border < right_border and top_border < bottom_border :

            # go right
            for col in range(left_border, right_border):
                res.append(matrix[top_border][col])

            # go down
            for row in range(top_border, bottom_border):
                res.append(matrix[row][right_border])


            # go left
            for col in range(right_border, left_border, -1):
                res.append(matrix[bottom_border][col])

            # go up
            for row in range(bottom_border, top_border, -1):
                res.append(matrix[row][left_border])


            # adjust borders
            right_border -= 1
            left_border += 1
            
            top_border += 1
            bottom_border -= 1

        # if there is 1D array left, traverse it

        # right_border = 2
        # left_border = 0

        # top = 1
        # bottom = 1

        if len(res) < TOTAL_ELEMENTS:
            for row in range(top_border, bottom_border + 1):
                for col in range(left_border, right_border + 1):
                    res.append(matrix[row][col])

        return res





