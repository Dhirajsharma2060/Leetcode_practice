class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            # if we have something like eat , tea , or ate === ate ,by sorted it into ate 
            key=''.join(sorted(s))
            #if the ate comes again then 
            ans[key].append(s)
            #return a list 
        return list(ans.values())    


        