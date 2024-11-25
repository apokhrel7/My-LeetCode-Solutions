from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # use bfs to traverse adjacent lands horizontally or vertically
        # for ex2 to work, have to go through entire grid then apply bfs to each one (dont visit lands already visited)

        # Constants
        ROWS = len(grid)
        COLS = len(grid[0])


        visited = set() # keeps track of visited coordinates

        def bfs(r, c):
            
            q = deque()
            q.append((r, c))


            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            # loop as long as you see adjacent islands (which are ready in the queue)
            while q:
                r, c = q.popleft()

                for dx, dy in DIRECTIONS:
                    new_r, new_c = r + dx, c + dy

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                        q.append((new_r, new_c))    # this land might have adjacent lands, so add it to queue
                        visited.add((new_r, new_c)) # mark this land as visited


        count_num_islands = 0

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == '1':
                    count_num_islands += 1  # only increments if new island is found (done by the conditional logic above)
                    visited.add((i, j))
                    bfs(i, j)

        return count_num_islands


        


        