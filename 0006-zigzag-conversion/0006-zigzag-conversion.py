class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
        i=0
        d=1# this is for direction it means that the d is downward until we reach the end and we have to move up
        result=[[] for _ in range(numRows)]
        for char in s:
            result[i].append(char)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i+=d
        ret=''
        for i in range(numRows):
            ret+=''.join(result[i])
        return ret                



        