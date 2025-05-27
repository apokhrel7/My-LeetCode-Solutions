from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """
        - every region of 'O's must be surrounded by 'X's (up, down, left, right)
        - if above isn't satisfied, then leave the 'O's uncaptured 
        - so just branch off of 'O's when none of them are touching the edge
        - first try to find a region of 'O's and only change them if none of them touch an edge
        - once you have branched out and even one (row, col) of an region touches the edge, then break out immediately
        - if not them, have the position of all the 'O's in that region tracked and change them to 'X's
        """
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        visited = set()

        def bfs(r, c):

            q.append((r, c))

            DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:
                i, j = q.popleft()

                for x, y in DIRECTIONS:
                    new_i, new_j = i + x, j + y

                    if (
                        0 <= new_i < ROWS
                        and 0 <= new_j < COLS
                        and (new_i, new_j) not in visited
                        and board[new_i][new_j] == "O"
                    ):
                        board[new_i][new_j] = "T"
                        visited.add((new_i, new_j))
                        q.append((new_i, new_j))

        # mark unsurrounded Os as Ts
        for row in range(ROWS):
            for col in range(COLS):
                if (
                    (row, col) not in visited
                    and board[row][col] == "O"
                    and (row == 0 or row == (ROWS - 1) or col == 0 or col == (COLS - 1))
                ):
                    board[row][col] = "T"
                    visited.add((row, col))
                    bfs(row, col)

        # Mark remaining Os as Xs
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

                elif board[row][col] == "T":
                    board[row][col] = "O"

        # # Unmark the Ts with Os
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if board[row][col] == "T":
        #             board[row][col] = "O"
