from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
                
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(image), len(image[0])
        q = deque([(sr, sc)])

        # save the target color
        original_target = image[sr][sc]
        image[sr][sc] = color 

        seen = set()
        

        while q:
            i, j = q.popleft()
            for x, y in DIRECTIONS:
                new_i, new_j = i + x, j + y

                if (new_i, new_j) not in seen and 0 <= new_i < ROWS and 0 <= new_j < COLS and image[new_i][new_j] == original_target:
                    image[new_i][new_j] = color
                    q.append((new_i, new_j))
                    seen.add((new_i, new_j))

        return image



            