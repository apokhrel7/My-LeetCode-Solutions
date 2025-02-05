from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()  # track which islands have been visited

        q = deque()

        # find out which grids contain an island, then span out to "see" how big it is
        # this way count that island as 1 island
        # look for others
        def bfs(r, c):
            DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            q.append((r, c))

            while q:
                row, col = q.popleft()
                for x, y in DIRECTIONS:
                    new_row, new_col = row + x, col + y

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == "1": 
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col)) 
                        
        num_islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    bfs(row, col)
                    num_islands += 1 

        


        return num_islands


        
