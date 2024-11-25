from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        
        def bfs(queue, count):
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # q = deque()
            # q.append((r, c))
            time_elapsed = 0

            while queue and count > 0:

                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dx, dy in DIRECTIONS:
                        new_r, new_c = r + dx, c + dy

                        if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1:
                            queue.append((new_r, new_c))
                            grid[new_r][new_c] = 2
                            count -= 1
                time_elapsed += 1

            return time_elapsed, count


        q = deque()
        fresh_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time_elapsed, fresh_count = bfs(q, fresh_count)
        return time_elapsed if fresh_count == 0 else -1


