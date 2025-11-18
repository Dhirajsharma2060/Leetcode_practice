class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        n=len(s)    
        longest=s[0]
        for i in range(n):
            for j in range(i+1,n):
                substr=s[i:j+1]
                if substr==substr[::-1]:
                    if len(substr)>len(longest):
                        longest=substr
        return longest                