class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time=0
        for i in range(len(timeSeries)-1):
            diff=timeSeries[i+1]-timeSeries[i]
            total_time+=min(diff,duration)
        total_time+=duration
        return total_time   

            


        