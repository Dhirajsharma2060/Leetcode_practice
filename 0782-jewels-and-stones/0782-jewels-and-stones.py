class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        group=set(jewels)
        for stone in stones:
            if stone in group:
                res+=1
        return res        


        