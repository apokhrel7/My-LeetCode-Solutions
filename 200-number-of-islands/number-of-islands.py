from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

    
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))

            DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            while q:
                r, c = q.popleft()
               
                for x, y in DIRECTIONS:
                    new_r, new_c = r + x, c + y

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))


        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    num_islands += 1
                    bfs(r, c)

        return num_islands

        


            