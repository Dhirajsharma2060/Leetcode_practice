class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            startFirst=firstList[i][0]
            endFirst=firstList[i][1]
            startSecond=secondList[j][0]
            endSecond=secondList[j][1]
            # this is not the first point overlap 
            if endFirst>=startSecond and endSecond>=startFirst:
                # note the max of the start and min of the end
                res.append([max(startFirst, startSecond), min(endFirst, endSecond)])
                
            if endFirst < endSecond:
                i+=1
            else:    
                j+=1
        return res            
        