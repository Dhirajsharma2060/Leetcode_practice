class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mapped={}
        dup=0
        for i in range(len(nums)):
            if nums[i] not in mapped:
                mapped[nums[i]]=i
            else:
                dup=nums[i]

        for x in  range(1,len(nums)+1):
            if x not in mapped:
                return [dup,x]        
        