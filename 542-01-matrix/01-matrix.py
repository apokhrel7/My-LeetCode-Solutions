from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        
        visited = set()
        q = deque()


        # Find a 1 and BFS on that??
        # if no 0 found, then increase distance count

        def bfs():
            DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            while q:
                row, col = q.popleft()

                for x, y in DIRECTIONS:
                    new_row, new_col = row + x, col + y

                    # maybe start from 0 and find 1 instead???
                    # if (new_row, new_col) is in bounds and if it's a 1, we still search for a 1 marked as #
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and mat[new_row][new_col] == "#":
                        mat[new_row][new_col] = mat[row][col] + 1
                        q.append((new_row, new_col))

                    

        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 1:
                    mat[row][col] = "#"
                    
                else:
                    q.append((row, col))

        bfs()
        return mat
        