class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for char in  strs:
                if i==len(char) or char[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]

                    
        