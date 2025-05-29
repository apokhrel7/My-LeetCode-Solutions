class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        1 -> 2
        n = 3: 1 -> 3, 2 -> 3, thus town judge is 3
        n = 3, 1 - > 3, 2 -> 3, 3 -> 1 (there is a cycle)
        in_degree[3]: 2
        # keep track of in degree and out degree
        # judge is found when it has all edges going to it, and none going out of it
        """

        # keep track of the number of incoming edges and outgoing edges for every people labeled from 1 to n
        # must do (n+1) since the labels start from 1..n (disregard the 0th index and use 1st index instead making it n numbers used)
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        # a_i = node that has an edge going out to b_i (out degree)
        # b_i = node that has an edge coming towards it from b_i (in degree)
        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, n + 1):
            # if there is a node with no out degree and every other node has an edge going towards it, this is the town judge (leaf node)
            if out_degree[i] == 0 and in_degree[i] == (n-1):
                return i

        return -1

        

        

