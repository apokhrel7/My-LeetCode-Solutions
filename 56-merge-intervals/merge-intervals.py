class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()  # sorts it by the beginning number
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1] = [min(intervals[i][0], merged[-1][0]), max(intervals[i][1], merged[-1][1])]

            else:
                merged.append(intervals[i])


        return merged






