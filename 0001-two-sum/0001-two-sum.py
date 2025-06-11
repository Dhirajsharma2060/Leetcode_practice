class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            #example 3,2,3,1
            #so hash map should be {3:0,2:1,3:2,1:3}
            #but if we do h[nums[i]]=i then {3:2,2:1,1:3}
            h[nums[i]]=i
        for i in  range(len(nums)):
            val=target-nums[i]
            if val in h and h[val]!=i:
                return [h[val],i]


        #time complexity is o(n^2)
        #space complexity is o(n)