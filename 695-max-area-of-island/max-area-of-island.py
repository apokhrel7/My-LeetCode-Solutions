from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            q = deque([(r, c)])
            DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            curr_area = 1  # this is one because if this method is called, there has been at least one island found

            while q:
                i, j = q.popleft()

                for x, y in DIRECTIONS:
                    new_i, new_j = i + x, j + y

                    # if (
                    #     0 <= new_i < ROWS
                    #     and 0 <= new_j < COLS
                    #     and (new_i, new_j) not in visited
                    #     and grid[new_i][new_j] == 1
                    # ):
                    #     curr_area += 1
                    #     q.append((new_i, new_j))
                    #     visited.add((new_i, new_j))
                    if (
                        0 <= new_i < ROWS
                        and 0 <= new_j < COLS
                        and grid[new_i][new_j] == 1
                    ):
                        curr_area += 1
                        q.append((new_i, new_j))
                        grid[new_i][new_j] = -1

            return curr_area

        for row in range(ROWS):
            for col in range(COLS):
                # if (row, col) not in visited and grid[row][col] == 1:
                #     visited.add((row, col))
                #     max_area = max(max_area, bfs(row, col))
                if grid[row][col] == 1:
                    grid[row][col] = -1
                    max_area = max(max_area, bfs(row, col))

        return max_area
