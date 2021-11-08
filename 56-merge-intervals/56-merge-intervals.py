class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) > 1:
            intervals = sorted(intervals, key = lambda x: x[0]) 
            
            
            IntervalToMerge = 0
            
            for curInterval in range(1, len(intervals)):
                if intervals[curInterval][0] <= intervals[IntervalToMerge][1]:
                    intervals[IntervalToMerge][1] = max(intervals[curInterval][1], intervals[IntervalToMerge][1])
                    intervals[curInterval] = None
                else:
                    IntervalToMerge = curInterval
            
        return([ i for i in intervals if i ])
        
        
        