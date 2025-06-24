class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            val=num*num
            res.append(val)
        return sorted(res)         

        