class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # centre graph must have out degree of n-1

        degrees = [0] * (10**5 + 1)

        max_edge = 0
        star_index = 0
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1

        for i in range(1, len(degrees)):
            if degrees[i] > max_edge:
                star_index = i
                max_edge = degrees[i]

        return star_index
