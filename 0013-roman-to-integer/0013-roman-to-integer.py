class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        for i in range(len(s)-1):
            if Symbol[s[i]]<Symbol[s[i+1]]:
                ans -= Symbol[s[i]]
            else:
                ans += Symbol[s[i]]
        ans += Symbol[s[-1]]    
        return ans                   
#time complexity is o(N)
#space complexity is o(1) because of the sysmbol dictnary size is fixed to 7                

        