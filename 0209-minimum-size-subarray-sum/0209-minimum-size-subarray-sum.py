class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=0
        min_size=float('inf')
        low=0
        n=len(nums)
        for high in range(n):
            window_sum+=nums[high]
            while window_sum>=target:
                #agar the window ka size equal ho gaya to target 
                min_size = min(min_size, high - low + 1)
                window_sum -= nums[low]
                low+=1
            
        if min_size == float('inf'):
            return 0
        else:
            return min_size



        