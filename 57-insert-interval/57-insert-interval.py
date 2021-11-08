class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return([newInterval])
        
        if newInterval[0] <= intervals[0][0]: ## If new interval starts at or before the first one, add new interval at the beginning
            intervals = [newInterval] + intervals
            startMergeFrom = 0
        elif newInterval[0] >= intervals[-1][0]: ## If new interval starts at or after the last one, add new interval at the end
            intervals.append(newInterval)
            startMergeFrom = len(intervals) - 2
        else:   ## Else, binary search for an apt place
            l, r = 0, len(intervals)-1 ## pair binary search
            m = (l+r)// 2
            while l < r:
                print(m)
                if  intervals[m+1][0] < newInterval[0]:
                    l = m+1
                elif intervals[m][0] > newInterval[0]:
                    r = m
                # elif intervals[m][0] <= newInterval[0] <= intervals[m+1][0]:
                else:
                    break
                m = (l+r)// 2
            
            
            
            ## Check if you need not merge with intervals at m or m+1
            if newInterval[0] > intervals[m][1] and newInterval[1] < intervals[m+1][0]:
                intervals.insert(m+1, newInterval)
                return(intervals)
            ## else merge in place to avoid the costly step of O(n)
            if intervals[m][1] >= newInterval[0]:
                intervals[m][1] = max( intervals[m][1],  newInterval[1])    ### Merge in place to avoid the extra step of costly O(n) insert
                startMergeFrom = m
            elif newInterval[1] >= intervals[m+1][0]:
                ## ideally it should be intervals[m+1][0] =min(intervals[m+1][0], newInterval[0]) but we already know newInterval[0]<=intervals[m+1][0] from binary search
                intervals[m+1][0] = newInterval[0] 
                intervals[m+1][1] = max( intervals[m+1][1],  newInterval[1]) ### Merge in place to avoid the extra step of costly O(n) insert
                startMergeFrom = m+1

        #### only start merging from 'startMergeFrom' point. No need to merge before that
        IntervalToMerge = startMergeFrom
        for curInterval in range(IntervalToMerge+1, len(intervals)):
            # print(intervals)
            # print(curInterval, intervals[curInterval], intervals[IntervalToMerge])
            if intervals[curInterval][0] <= intervals[IntervalToMerge][1]:
                intervals[IntervalToMerge][1] = max(intervals[IntervalToMerge][1], intervals[curInterval][1])
                intervals[curInterval] = None               ### Place n instead of doing costly O(n) delete after every merge --> O(n^2)
            else:
                curInterval = IntervalToMerge
                
        return([i for i in intervals if i])
        
        
                    
                
            
        
        