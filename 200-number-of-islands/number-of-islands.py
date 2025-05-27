from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def bfs(r, c):
            DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            q.append((r, c))

            while q:
                i, j = q.popleft()

                for x, y in DIRECTIONS:
                    new_i, new_j = i + x, j + y
                    
                    if 0 <= new_i < ROWS and 0 <= new_j < COLS and (new_i, new_j) not in seen and grid[new_i][new_j] == '1':
                        seen.add((new_i, new_j))
                        q.append((new_i, new_j))

        
        # loop through entire grid and expand out when island is found
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in seen and grid[row][col] == '1':
                    # expand on this (row, col) using BFS
                    # track the (row, col) that you have expanded on
                    num_islands += 1
                    seen.add((row, col))
                    bfs(row, col)

        return num_islands
        

        