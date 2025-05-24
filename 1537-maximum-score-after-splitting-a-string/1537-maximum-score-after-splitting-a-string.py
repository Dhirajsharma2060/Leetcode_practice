class Solution:
    def maxScore(self, s: str) -> int:
        left=""
        right=""
        summation=0
        max_score=0
        for i in range(1,len(s)):
            left=s[:i].count('0')
            right=s[i:].count('1')
            summation=left+right
            max_score=max(summation,max_score)  
        return max_score    

        