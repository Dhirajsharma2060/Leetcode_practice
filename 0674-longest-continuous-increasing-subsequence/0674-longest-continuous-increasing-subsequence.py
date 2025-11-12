class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        window_size=1
        max_window=1
        if not nums:
            return 0
             
        for right in range(len(nums)-1):
            if nums[right]<nums[right+1]:
                window_size+=1
            else:
                window_size=1 
            max_window=max(max_window,window_size)           
        return max_window     



        