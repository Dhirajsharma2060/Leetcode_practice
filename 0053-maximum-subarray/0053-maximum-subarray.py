class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # best_ending=nums[0]
        # ans=nums[0]
        # for i in range(1,len(nums)):
        #     v1=best_ending+nums[i]
        #     v2=nums[i]
        #     best_ending=max(v1,v2)
        #     ans=max(ans,best_ending)
        # return ans  
        minend=nums[0]
        maxend=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=maxend+nums[i]
            v3=minend+nums[i]
            maxend=max(v1,v2)
            minend=min(v1,v3)
            ans=max(ans,maxend,minend)
        return ans    

