class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        runningSum=[0]*n
        runningSum[0]=nums[0]
        for i in range(1,n):
            runningSum[i]=runningSum[i-1]+nums[i]
        return runningSum    

        