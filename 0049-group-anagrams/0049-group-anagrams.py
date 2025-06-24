from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            #we no need to check wheather the key is there or not in dictnary we using default dict ok
            ans[key].append(s)  
        return list(ans.values())      