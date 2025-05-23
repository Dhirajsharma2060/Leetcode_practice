class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        CloseNum=nums[0]
        for i in nums:
            if abs(i)<abs(CloseNum):
                CloseNum=i
        #followinf part jho hai vho is liye hai kiyu ki agar 2 number ek negative and ek positive ha but dono closer hai 0 ke then we will chose the Close value 
        if CloseNum<0 and abs(CloseNum) in nums:
            return abs(CloseNum)
        return CloseNum            

        