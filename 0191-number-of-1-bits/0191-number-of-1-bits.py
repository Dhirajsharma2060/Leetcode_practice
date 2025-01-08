class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        value=bin(n)
        #note:Python bin use karke int to binary  string me convert karta hai 
        for num in value:
            if num=='1':
                res=res+1
        return res        
        