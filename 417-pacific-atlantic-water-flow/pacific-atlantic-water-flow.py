from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        - do the opposite (go to each cell which you cant flood and mark them)
        - go to each of those cells and branch out
        - now the remaining unmarked cells are the ones you can go to in terms of pacific and atlantic ocean
        - 
        """
        # If 2D has not cols or just has nothing in it, returning nothing
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacific_q, atlantic_q = deque(), deque()

        # Boolean grids: reachable[i][j] == True means water can flow from (i,j) to that ocean
        pacific_reachable, atlantic_reachable = [], []

        for row in range(ROWS):
            pacific_reachable.append([False] * COLS)
            atlantic_reachable.append([False] * COLS)

        # 1) Seed both queues with all the border cells
        #    - top row & left column for Pacific
        #    - bottom row & right column for Atlantic
        for row in range(ROWS):
            pacific_q.append((row, 0))
            pacific_reachable[row][0] = True

            atlantic_q.append((row, COLS - 1))
            atlantic_reachable[row][COLS-1] = True

        ## for top and bottom
        for col in range(COLS):
            pacific_q.append((0, col))
            pacific_reachable[0][col] = True

            atlantic_q.append((ROWS - 1, col))
            atlantic_reachable[ROWS - 1][col] = True
        

        # 2) BFS helper: flood "uphill" from the queued cells (from the outside borders),
        ##    marking every neighbor we can reach (i.e. heights[ni][nj] >= heights[i][j]).
        def bfs(q, visited):
            DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

            while q:
                i, j = q.popleft()

                for x, y in DIRECTIONS:
                    new_i, new_j = i + x, j + y

                    # check if new cell is in bounds, not visited, and if the new cell is bigger or equal to the previous one  
                    if 0 <= new_i < ROWS and 0 <= new_j < COLS and not visited[new_i][new_j] and heights[new_i][new_j] >= heights[i][j]:
                        visited[new_i][new_j] = True
                        q.append((new_i, new_j))
                        

        # 3) Run uphill‐BFS from both oceans’ borders
        bfs(pacific_q, pacific_reachable)
        bfs(atlantic_q, atlantic_reachable)

        # 4) Any cell reachable by both floods can send water to both oceans
            ## The intersection of the pacific visited and atlantic visited will give us the coordinates of the cells where water 
            ## can flow to both Pacific and Atlantic oceans
        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                    res.append([row, col])

        return res 



         



