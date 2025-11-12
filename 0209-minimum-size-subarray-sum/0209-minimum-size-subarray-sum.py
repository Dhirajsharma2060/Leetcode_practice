class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_size=0
        left=0
        min_length=float('inf')
        n=len(nums)
        for right in range(n):
            window_size+=nums[right]
            while window_size>=target:
                min_length=min(min_length,right-left+1)
                window_size-=nums[left]
                left+=1
        return min_length if min_length!=float('inf') else 0        
