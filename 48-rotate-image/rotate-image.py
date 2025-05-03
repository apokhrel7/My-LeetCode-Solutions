class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Reverse the columns
        # Transpose

        length = len(matrix)

        top = 0
        bottom = length - 1

        # reverse matrix vertically (reverse each column)
        while top < bottom:
            for col in range(length):
                matrix[top][col], matrix[bottom][col]  = matrix[bottom][col], matrix[top][col]
            
            top += 1 # go down the column
            bottom -= 1  # go up the column

        # transpose so that each (i, j) becomes (j, i)
        for row in range(length):
            for col in range(row+1, length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        return matrix

        
        