class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        smallest=[]
        n=len(nums)
        if not nums: return smallest
        start=nums[0]
        for i in range(1,n+1):
            if i==len(nums) or nums[i] != nums[i-1]+1:
                if start==nums[i-1]:
                    smallest.append(str(start))
                else:
                    smallest.append(f"{start}->{nums [i-1]}")
                if i <len(nums):
                    start=nums[i]
        return smallest                           
                    


        return smallest    
        