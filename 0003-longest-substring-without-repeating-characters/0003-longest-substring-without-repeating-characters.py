class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        left=0
        count=set()
        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left+=1
            count.add(s[right])
            longest=max(longest,right-left+1)
        return longest    


