from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use bfs
        # dict = {}
        # for i in range(len(word)):
        #     if word[i] not in dict:
        #         dict[word[i]] = 0

        #     else:
        #         dict[word[i]] += 1

        ROWS, COLS = len(board), len(board[0])

        seen = set()
        

        def dfs(r, c, i):

            # if i has exceeded its limit, then all letters have been found (guaranteed went through i=0...n-1) 
            if i == len(word):
                return True

            # if row OR column out of bounds, OR position (r, c) already seen in path, 
            # OR current letter in board (board[r][c]) doesn't match current letter in word 
            # If above conditions passed, return False as condition not met 
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or board[r][c] != word[i]:
                return False

            # Add position (r, c) of the grid board into set of seen coordinates
            seen.add((r, c))

            # below is almost like BFS branching out up, down, left, right
            res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)

            # remove seen paths as to backtrack to possibly find other valid paths
            seen.remove((r, c))

            # return result: True or False whether word exists in the grid (i.e. is there a path on the grid that mathces the target word)
            return res

        # Go through each character of the grid and apply DFS to find a possible path that leads to the target "word"
        for i in range(ROWS):
            for j in range(COLS):
                
                # if DFS returns True, then "word" exists in the grid
                if dfs(i, j, 0):
                    return True

                
        return False
                




       

