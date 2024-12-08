class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest=0
        seen=set()
        for c in s:
            if c in seen:
                seen.remove(c)
                longest+=2#yaha pe ham remove kar rahe hai jab hum usse 2 nd dekh rahe hongeb so longest+=2
            else:
                seen.add(c)
        return longest+1 if seen else longest            
 
             
        