class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        curr=0
        for num in nums:
            curr=(curr<<1)+num
            res.append(curr%5==0)
        return res    

        