class Solution:
    def numSub(self, s: str) -> int:
        count_one=0
        res=count_one
        for c in s :
            if c=="1":
                count_one+=1
                res+=count_one
            else:
                count_one=0
        return res % (10**9 +7)   

        