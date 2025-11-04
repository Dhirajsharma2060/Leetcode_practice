class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        newstart,newend=newInterval
        n=len(intervals)
        i=0
        # the new interval se pehle wale
        while i < n and intervals[i][1]<newstart:
            res.append(intervals[i])
            i+=1


        # newInterval add hoga if no overlap the alsp res.appendhoga    
        while i <n and intervals[i][0]<=newend:
            newstart=min(newstart,intervals[i][0])
            newend=max(newend,intervals[i][1])
            i+=1
        res.append([newstart,newend])

        #newInterval ke bad ka 
        while i<n :
            res.append(intervals[i])
            i+=1
        return res        

