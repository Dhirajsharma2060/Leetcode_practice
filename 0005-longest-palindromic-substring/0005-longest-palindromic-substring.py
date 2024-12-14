#this is the bute force approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(sub:str)->bool:
            return sub==sub[::-1]
        
        n=len(s)
        if n<=1:
            return s

        result=""
        if s==1:
            result+=s
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if isPalindrome(substring) and len(substring)>len(result):
                    result=substring
        return result             


        