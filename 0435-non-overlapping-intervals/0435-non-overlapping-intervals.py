class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort(key=lambda i:i[0])
        prevend=intervals[0][1]
        for start , end in intervals[1:]:
            if start<prevend:
                count+=1
                prevend = min(prevend, end)
            else:
                prevend=end    
        return count        
        