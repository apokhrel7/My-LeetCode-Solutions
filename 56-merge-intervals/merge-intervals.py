class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        # first sort intervals
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1] = [min(merged[-1][0], intervals[i][0]), max(merged[-1][1], intervals[i][1])]
            else:
                merged.append(intervals[i])

        return merged

            
         
                

            
            
            


        