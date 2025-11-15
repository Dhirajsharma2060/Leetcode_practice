class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_one=count
        left=0
        for right in range(len(nums)):
            if nums[right]==1:
                count+=1
                max_one=max(max_one,count)
            else:
                count=0
        return max_one            

        