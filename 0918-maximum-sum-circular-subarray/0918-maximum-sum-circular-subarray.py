class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        maxend=nums[0]
        minend=nums[0]
        ansmax=nums[0]
        ansmin=nums[0]
        ans=nums[0]
        # first lets find the maximum
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=maxend+nums[i]
            v3=minend+nums[i]

            maxend=max(v1,v2)
            minend=min(v1,v3)

            ansmax = max(ansmax, maxend)   # maximum subarray sum
            ansmin = min(ansmin, minend)   # minimum subarray sum
        if ansmax<0:
            return ansmax
        # Circular sum = total - minimum subarray
        return max(ansmax, total - ansmin)




