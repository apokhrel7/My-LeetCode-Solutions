class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # go right
        # go down
        # go left
        # go up

        right = len(matrix[0]) - 1
        left = 0
        top = 0
        bottom = len(matrix) - 1


        res = []

        
        while top < bottom and left < right:

            for i in range(left, right):
                res.append(matrix[top][i])

            for i in range(top, bottom):
                res.append(matrix[i][right])

            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])

            right -= 1
            left += 1
            top += 1
            bottom -= 1

        if top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])

        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])

        return res

                
        