class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=len(nums)
        min_val=0
        running_sum=0
        for i in range(n):
            running_sum+=nums[i]
            min_val=min(min_val,running_sum) 
        return -min_val+1       
        