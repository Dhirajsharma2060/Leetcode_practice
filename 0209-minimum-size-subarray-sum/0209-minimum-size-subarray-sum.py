class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        window_size=0
        left=0
        for right in range(len(nums)):
            window_size+=nums[right]
            while window_size>=target:
                min_length=min(min_length,right-left+1)
                window_size-=nums[left]
                left+=1
        return 0 if min_length==float('inf') else min_length        
        