class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>0:
            #why 5 becuause to get zero we need 10 which = 2*5 so the most non common are 5 
            n//=5
            #why n 26 n//=5 -> 5 count=5 menase to we need 5 5 to make colser to 26 and +1 later for second iteration n=1 n//=5 i.e 1//5 -> 0 count+=1 so 25+1
            count+=n
        return count 
        