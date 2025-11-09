class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        product=1
        res=0
        for r in range(n):
            product*=nums[r]
            if k<=1:
                return 0
            while product>=k:
                product=product//nums[l]
                l+=1
            res+=(r-l+1)    
        return res     
           

        
        