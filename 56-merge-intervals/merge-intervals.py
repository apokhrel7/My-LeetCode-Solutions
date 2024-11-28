class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        overlap = [intervals[0]]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= overlap[-1][1]:
                overlap[-1] = min(intervals[i][0], overlap[-1][0]), max(intervals[i][1], overlap[-1][1])

            else:
                overlap.append(intervals[i]) 

        return overlap